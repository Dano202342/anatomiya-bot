"""Anatomiya o'quv boti — odam tanasini 3D rasm va animatsiyalar bilan o'rgatadi."""

import asyncio
import json
import logging
import os
import re
import socket
from pathlib import Path

import aiohttp
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ChatAction, ParseMode
from aiogram.exceptions import TelegramBadRequest, TelegramForbiddenError
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import (BufferedInputFile, CallbackQuery, FSInputFile, InlineKeyboardButton,
                           InlineKeyboardMarkup, KeyboardButton, Message, ReplyKeyboardMarkup, WebAppInfo)
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent / ".env")

import media  # noqa: E402
import quiz  # noqa: E402
import stats  # noqa: E402
import webserver  # noqa: E402
from content import SECTIONS, all_items, get_category, get_item  # noqa: E402

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("anatomiya")

FILE_IDS_JSON = media.DATA_DIR / "file_ids.json"
try:
    file_ids: dict = json.loads(FILE_IDS_JSON.read_text(encoding="utf-8"))
except (FileNotFoundError, json.JSONDecodeError):
    file_ids = {}

dp = Dispatcher()
dp.include_router(quiz.router)


@dp.update.outer_middleware()
async def _track_users(handler, event, data):
    user = data.get("event_from_user")
    if user and not user.is_bot:
        await stats.track(user.id)
    return await handler(event, data)
http: aiohttp.ClientSession | None = None

# Foydalanuvchi qayerda turgani — "⬅️ Orqaga" tugmasi uchun
nav: dict[int, tuple] = {}

MENU_BUTTONS = {s["title"]: k for k, s in SECTIONS.items()}
ATLAS_BTN = "🧊 3D atlas"
QUIZ_BTN = "🎯 Viktorina"
CHANNEL_BTN = "📢 Kanalimiz"
SEARCH_BTN = "🔎 Qidirish"
HELP_BTN = "ℹ️ Yordam"
BACK_BTN = "⬅️ Orqaga"
HOME_BTN = "🏠 Bosh menyu"


# ───────────────────────── Klaviaturalar ─────────────────────────

def main_menu() -> ReplyKeyboardMarkup:
    t = [KeyboardButton(text=x) for x in MENU_BUTTONS]
    rows = [t[i:i + 2] for i in range(0, len(t), 2)]
    extra = [KeyboardButton(text=QUIZ_BTN), KeyboardButton(text=ATLAS_BTN)]
    if channel_url():  # Vercel'da CHANNEL_URL=https://t.me/kanal_nomi
        extra.append(KeyboardButton(text=CHANNEL_BTN))
    rows.append(extra)
    rows.append([KeyboardButton(text=BACK_BTN), KeyboardButton(text=SEARCH_BTN), KeyboardButton(text=HELP_BTN)])
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True,
                               input_field_placeholder="Bo'limni tanlang yoki nom yozing...")


HOME_IB = InlineKeyboardButton(text=HOME_BTN, callback_data="home")


def section_kb(sec: str) -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text=c["title"], callback_data=f"c|{sec}|{c['key']}")]
            for c in SECTIONS[sec]["categories"]]
    rows.append([HOME_IB])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def category_kb(sec: str, cat: str) -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text=("🧊 " if webserver.has_anim(sec, i["key"]) else "") + i["title"],
                                  callback_data=f"i|{sec}|{cat}|{i['key']}")]
            for i in get_category(sec, cat)["items"]]
    rows.append([InlineKeyboardButton(text=BACK_BTN, callback_data=f"s|{sec}"), HOME_IB])
    return InlineKeyboardMarkup(inline_keyboard=rows)


def item_kb(sec: str, cat: str, it: dict) -> InlineKeyboardMarkup:
    items = get_category(sec, cat)["items"]
    idx = next(n for n, x in enumerate(items) if x["key"] == it["key"])
    l = media.links(it)
    rows = []
    url = webserver.public_url()
    if url:
        label = ("🧊 3D modelni aylantirish (bot ichida)" if webserver.has_anim(sec, it["key"])
                 else "🔍 Rasmni kattalashtirib ko'rish")
        rows.append([InlineKeyboardButton(text=label, web_app=WebAppInfo(url=f"{url}/?v={sec}/{it['key']}"))])
    rows.append([InlineKeyboardButton(text="🎬 Video darslar", url=l["video"]),
                 InlineKeyboardButton(text="🌐 Sketchfab 3D", url=l["3d"])])
    nav_row = []
    if idx > 0:
        nav_row.append(InlineKeyboardButton(text="◀️ Oldingi", callback_data=f"i|{sec}|{cat}|{items[idx - 1]['key']}"))
    if idx < len(items) - 1:
        nav_row.append(InlineKeyboardButton(text="Keyingi ▶️", callback_data=f"i|{sec}|{cat}|{items[idx + 1]['key']}"))
    if nav_row:
        rows.append(nav_row)
    rows.append([InlineKeyboardButton(text=BACK_BTN, callback_data=f"c|{sec}|{cat}"), HOME_IB])
    return InlineKeyboardMarkup(inline_keyboard=rows)


# ───────────────────────── Media yuborish ─────────────────────────

def _remember(key: str, file_id: str) -> None:
    file_ids[key] = file_id
    try:  # Vercel'da disk faqat o'qish uchun — u yerda xotirada qoladi
        media.DATA_DIR.mkdir(exist_ok=True)
        FILE_IDS_JSON.write_text(json.dumps(file_ids, indent=1), encoding="utf-8")
    except OSError:
        pass


async def _upload_file(src, name: str):
    """Mahalliy fayl yoki yuklab olingan baytlar — havola ishlamaganda zaxira yo'l."""
    if isinstance(src, Path):
        return FSInputFile(src)
    data = await media.download(http, src)
    if not data:
        return None
    if not os.path.splitext(name)[1]:
        name += ".gif"
    return BufferedInputFile(data, filename=name.replace(" ", "_"))


async def _send(msg: Message, kind: str, src, caption: str) -> None:
    """Tezlik tartibi: saqlangan file_id → havola (Telegram o'zi oladi) → yuklab yuborish."""
    path_or_url, name = src
    key = str(path_or_url)
    send = msg.answer_animation if kind == "anim" else msg.answer_photo
    tries = []
    if key in file_ids:
        tries.append(file_ids[key])
    if isinstance(path_or_url, str):
        tries.append(path_or_url)
    tries.append(None)  # yuklab yuborish
    for f in tries:
        try:
            if f is None:
                f = await _upload_file(path_or_url, name)
                if f is None:
                    return
            sent = await send(f, caption=caption)
            obj = (sent.animation or sent.document) if kind == "anim" else sent.photo[-1]
            if obj:
                _remember(key, obj.file_id)
            return
        except TelegramBadRequest as e:
            log.warning("%s yuborilmadi (%s): %s", kind, key[:80], e)


async def _send_anim(msg: Message, it: dict, src) -> None:
    await _send(msg, "anim", src, f"🧊 <b>{it['title']}</b> — 3D model")


async def _send_photo(msg: Message, it: dict, src) -> None:
    await _send(msg, "photo", src, f"🖼 <b>{it['title']}</b>")


async def show_item(msg: Message, user_id: int, sec: str, cat: str, it: dict) -> None:
    nav[user_id] = ("item", sec, cat)
    await msg.bot.send_chat_action(msg.chat.id, ChatAction.UPLOAD_PHOTO)
    m = await media.get_media(http, sec, it)
    # Animatsiya va rasm bir vaqtda yuklanadi — tezroq
    await asyncio.gather(*([_send_anim(msg, it, m["anim"])] if m["anim"] else []),
                         *([_send_photo(msg, it, m["photo"])] if m["photo"] else []))
    text = f"<b>{it['title']}</b>\n🏷 <i>{it['lat']}</i>\n\n{it['text']}"
    await msg.answer(text, reply_markup=item_kb(sec, cat, it), disable_web_page_preview=True)


# ───────────────────────── Matnlar ─────────────────────────

WELCOME = """
👋 <b>Assalomu alaykum, {name}!</b>

Men — <b>Anatomiya boti</b> 🧬. Odam tanasini <b>3D modellar, animatsiyalar va rasmlar</b> bilan o'rgataman.

<b>Bo'limlar:</b>
🧠 <b>Nerv tizimi</b> — har bir nerv nomi bilan
💪 <b>Muskullar</b> — boshdan oyoqgacha
🧴 <b>Teri, soch va tuklar</b>
🦴 <b>Suyaklar</b> — 206 suyak va bo'g'imlar
🫘 <b>Buyrak va siydik tizimi</b>
❤️ <b>Qon aylanish tizimi</b>
🧪 <b>Bezlar va gormonlar</b>
🩺 Har bir bo'limda: <b>qayer buzilsa — qanday kasallik kelib chiqadi</b>

🧊 <b>3D atlas</b> — 3D modellarni bot ichida barmoq bilan aylantirib ko'ring!
🎯 <b>Viktorina</b> — 10 ta savol bilan bilimingizni sinang!

Pastdagi tugmalardan birini bosing 👇 yoki a'zo nomini yozing.
"""

HELP = """
<b>ℹ️ Botdan foydalanish</b>

1️⃣ Pastdagi tugmalardan bo'limni tanlang
2️⃣ Kichik bo'limni, so'ng mavzuni tanlang
3️⃣ Bot yuboradi: 🧊 3D animatsiya, 🖼 rasm va 📖 tushuntirish

<b>Tugmalar:</b>
🧊 <b>3D modelni aylantirish</b> — bot ichida ochiladi, barmoq bilan surib aylantirasiz, kattalashtirasiz
🧊 belgisi bor mavzularda aylanuvchi 3D model bor
◀️ ▶️ — oldingi / keyingi mavzu
⬅️ <b>Orqaga</b> — bir qadam orqaga
🏠 <b>Bosh menyu</b> — boshiga qaytish
🔎 <b>Qidirish</b> — nomni o'zbekcha, lotincha yoki inglizcha yozing
🎯 <b>Viktorina</b> — 10 ta savol, oxirida ball va baho

/start — bosh menyu
/quiz — viktorina
/help — yordam
"""


# ───────────────────────── Handlerlar ─────────────────────────

async def send_home(msg: Message, user_id: int, name: str | None = None):
    nav.pop(user_id, None)
    await msg.answer(WELCOME.format(name=name or "do'stim"), reply_markup=main_menu())


async def send_section(msg: Message, user_id: int, sec: str):
    nav[user_id] = ("sec", sec)
    await msg.answer(SECTIONS[sec]["intro"], reply_markup=section_kb(sec))


def category_text(sec: str, cat: str) -> str:
    c = get_category(sec, cat)
    return f"<b>{c['title']}</b>\n\n{c['intro']}\n\n👇 Mavzuni tanlang (🧊 — 3D modeli bor):"


@dp.message(CommandStart())
async def cmd_start(msg: Message, command: CommandObject):
    """/start yoki kanal tugmasidan kelgan deep link: t.me/<bot>?start=<payload>

    payload: quiz | quiz-<bo'lim|all> | atlas | s-<bo'lim> | i-<bo'lim>-<mavzu>
    """
    uid, arg = msg.from_user.id, (command.args or "").strip()
    parts = arg.split("-", 2)
    if parts[0] == "quiz":
        if len(parts) > 1 and (parts[1] == "all" or parts[1] in SECTIONS):
            await stats.quiz_started()
            return await quiz.ask(msg, parts[1], 0, 0)
        return await quiz.send_menu(msg)
    if parts[0] == "atlas":
        return await open_atlas(msg)
    if parts[0] == "s" and len(parts) == 2 and parts[1] in SECTIONS:
        await msg.answer("👋 Xush kelibsiz!", reply_markup=main_menu())
        return await send_section(msg, uid, parts[1])
    if parts[0] == "i" and len(parts) == 3 and (parts[1], parts[2]) in quiz.INDEX:
        cat, it = quiz.INDEX[(parts[1], parts[2])]
        await msg.answer("👋 Xush kelibsiz!", reply_markup=main_menu())
        return await show_item(msg, uid, parts[1], cat, it)
    await send_home(msg, uid, msg.from_user.first_name)


def is_admin(uid: int) -> bool:
    return uid in stats.admin_ids()


def not_admin_text(uid: int) -> str:
    names = list(stats.env_like("ADMIN"))
    # Diagnostika: raqamlarni to'liq oshkor qilmasdan nima o'qilganini ko'rsatamiz
    seen = ", ".join(f"{str(a)[:3]}…{str(a)[-2:]} ({len(str(a))} xona)" for a in stats.admin_ids()) or "raqam topilmadi"
    diag = "nomida ADMIN bor o'zgaruvchi yo'q ❌" if not names else f"{', '.join(names)} → {seen}"
    ver = (os.getenv("VERCEL_GIT_COMMIT_SHA") or "lokal")[:7]
    return (f"⛔️ Bu buyruq faqat bot egasi uchun.\n\n🆔 Sizning Telegram ID: <code>{uid}</code>\n"
            f"🔧 Bot ko'rgan admin sozlamasi: {diag}\n🔖 Versiya: {ver}\n\n"
            f"Agar bot egasi siz bo'lsangiz, Vercel'dagi <code>ADMIN_IDS</code> qiymati aynan shu raqam "
            f"ekanini tekshiring va Redeploy qiling.")


async def deep_link(msg: Message, payload: str) -> str:
    me = await msg.bot.me()
    return f"https://t.me/{me.username}?start={payload}"


@dp.message(Command("link"))
async def cmd_link(msg: Message, command: CommandObject):
    """Admin: kanal postlari uchun deep link havolalari. /link yoki /link femur"""
    if not is_admin(msg.from_user.id):
        return await msg.answer(not_admin_text(msg.from_user.id))
    q = (command.args or "").lower().strip()
    if not q:
        lines = [f"🎯 Viktorina menyusi:\n<code>{await deep_link(msg, 'quiz')}</code>",
                 f"🎲 Darhol aralash viktorina:\n<code>{await deep_link(msg, 'quiz-all')}</code>",
                 f"🧊 3D atlas:\n<code>{await deep_link(msg, 'atlas')}</code>"]
        lines += [f"{s['title']}:\n<code>{await deep_link(msg, 's-' + k)}</code>" for k, s in SECTIONS.items()]
        lines.append("\n💡 Aniq mavzu uchun: <code>/link son suyagi</code>")
        return await msg.answer("🔗 <b>Deep link havolalari</b>\n\n" + "\n\n".join(lines))
    hits = [(s, i) for s, c, i in all_items() if q in i["title"].lower() or q in i["lat"].lower() or q in i["en"].lower()]
    if not hits:
        return await msg.answer("Topilmadi.")
    lines = [f"{i['title']}:\n<code>{await deep_link(msg, f'i-{s}-' + i['key'])}</code>" for s, i in hits[:10]]
    await msg.answer("🔗 <b>Mavzu havolalari</b>\n\n" + "\n\n".join(lines))


def _channel_raw() -> str:
    """Nomida CHANNEL yoki KANAL bor o'zgaruvchi (CHANNEL_URL, CHANNEL_ID, KANAL ...)."""
    return next((v.strip().strip('"\'') for v in stats.env_like("CHANNEL", "KANAL").values() if v.strip()), "")


def channel_chat() -> str | None:
    """Kanalga post yuborish uchun: @nom yoki -100... ID."""
    v = _channel_raw()
    if re.fullmatch(r"-100\d+", v):
        return v
    name = v.rstrip("/").rsplit("/", 1)[-1].lstrip("@")
    return f"@{name}" if re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{3,}", name) else None


def channel_url() -> str | None:
    """Tugma uchun havola: https://t.me/nom"""
    chat = channel_chat()
    return f"https://t.me/{chat[1:]}" if chat and chat.startswith("@") else None


@dp.message(Command("post"))
async def cmd_post(msg: Message, command: CommandObject):
    """Admin: postga javob (reply) qilib yozing:  /post <payload> <tugma matni>
    Masalan:  /post quiz-all 🎯 Viktorinani boshlash"""
    if not is_admin(msg.from_user.id):
        return await msg.answer(not_admin_text(msg.from_user.id))
    usage = ("📝 <b>Kanalga tugmali post joylash</b>\n\n"
             "1. Postni (matn yoki rasm+matn) botga yuboring\n"
             "2. O'sha xabarga <b>javob (Reply)</b> qilib yozing:\n"
             "<code>/post quiz-all 🎯 Viktorinani boshlash</code>\n\n"
             "Payloadlar: <code>quiz</code>, <code>quiz-all</code>, <code>quiz-suyak</code>, <code>atlas</code>, "
             "<code>s-suyak</code>, <code>i-suyak-femur</code> (/link buyrug'i bilan oling)\n\n"
             "⚠️ Bot kanalda <b>admin</b> bo'lishi va post joylash huquqiga ega bo'lishi kerak.")
    args = (command.args or "").split(maxsplit=1)
    if not msg.reply_to_message or len(args) < 2:
        return await msg.answer(usage)
    chat = channel_chat()
    if not chat:
        return await msg.answer("❌ Kanal sozlanmagan: Vercel'ga <code>CHANNEL_URL</code> (yoki <code>CHANNEL_ID</code>) qo'shing.")
    payload, label = args
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=label, url=await deep_link(msg, payload))]])
    try:
        await msg.bot.copy_message(chat, msg.chat.id, msg.reply_to_message.message_id, reply_markup=kb)
    except (TelegramBadRequest, TelegramForbiddenError) as e:
        return await msg.answer(f"❌ Kanalga joylab bo'lmadi: {e.message}\n\nBot kanalda admin ekanini tekshiring.")
    await msg.answer(f"✅ Post {chat} kanaliga joylandi!")


@dp.message(Command("help"))
@dp.message(F.text == HELP_BTN)
async def cmd_help(msg: Message):
    await msg.answer(HELP, reply_markup=main_menu())


@dp.message(F.text == SEARCH_BTN)
async def ask_search(msg: Message):
    await msg.answer("🔎 Qidirmoqchi bo'lgan a'zo yoki kasallik nomini yozing.\n"
                     "Masalan: <i>yelka</i>, <i>femur</i>, <i>buyrak</i>, <i>diabet</i>, <i>insult</i>")


@dp.message(F.text == CHANNEL_BTN)
async def open_channel(msg: Message):
    url = channel_url()
    if not url:
        return await msg.answer("Kanal hali ochilmagan.", reply_markup=main_menu())
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="📢 Kanalga o'tish", url=url)]])
    await msg.answer("📢 Yangiliklar, qiziqarli anatomiya faktlari va yangi bo'limlar — kanalimizda!\n"
                     "Obuna bo'ling 👇", reply_markup=kb)


@dp.message(Command("stats"))
async def cmd_stats(msg: Message):
    admins = stats.admin_ids()
    if not admins:  # admin hali belgilanmagan — egasiga o'z ID sini ko'rsatamiz
        return await msg.answer(
            f"🆔 Sizning Telegram ID: <code>{msg.from_user.id}</code>\n\n"
            "Statistikani faqat siz ko'rishingiz uchun Vercel → Environment Variables ga\n"
            f"<code>ADMIN_IDS={msg.from_user.id}</code>\nqo'shing va Redeploy qiling.")
    if msg.from_user.id not in admins:
        return await msg.answer(not_admin_text(msg.from_user.id))
    await msg.answer(await stats.report())


@dp.message(F.text == QUIZ_BTN)
@dp.message(Command("quiz"))
async def open_quiz(msg: Message):
    await quiz.send_menu(msg)


@dp.message(F.text == ATLAS_BTN)
async def open_atlas(msg: Message):
    url = webserver.public_url()
    if not url:
        return await msg.answer("⏳ 3D ko'ruvchi hozir ishga tushmoqda, bir daqiqadan keyin qayta urinib ko'ring.")
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="🧊 3D atlasni ochish", web_app=WebAppInfo(url=url + "/"))]])
    await msg.answer("🧊 <b>3D anatomiya atlasi</b>\n\nBarcha 3D modellar bitta joyda — tanlang va barmoq bilan aylantiring.",
                     reply_markup=kb)


@dp.message(F.text == BACK_BTN)
async def go_back(msg: Message):
    uid = msg.from_user.id
    st = nav.get(uid)
    if st and st[0] == "item":
        nav[uid] = ("cat", st[1], st[2])
        return await msg.answer(category_text(st[1], st[2]), reply_markup=category_kb(st[1], st[2]))
    if st and st[0] == "cat":
        return await send_section(msg, uid, st[1])
    await send_home(msg, uid, msg.from_user.first_name)


@dp.message(F.text.in_(MENU_BUTTONS))
async def open_section(msg: Message):
    await send_section(msg, msg.from_user.id, MENU_BUTTONS[msg.text])


@dp.callback_query(F.data == "home")
async def cb_home(cq: CallbackQuery):
    await cq.answer()
    await send_home(cq.message, cq.from_user.id, cq.from_user.first_name)


@dp.callback_query(F.data.startswith("s|"))
async def cb_section(cq: CallbackQuery):
    sec = cq.data.split("|")[1]
    nav[cq.from_user.id] = ("sec", sec)
    await _edit_or_send(cq, SECTIONS[sec]["intro"], section_kb(sec))


@dp.callback_query(F.data.startswith("c|"))
async def cb_category(cq: CallbackQuery):
    _, sec, cat = cq.data.split("|")
    if not get_category(sec, cat):
        return await cq.answer("Topilmadi", show_alert=True)
    nav[cq.from_user.id] = ("cat", sec, cat)
    await _edit_or_send(cq, category_text(sec, cat), category_kb(sec, cat))


@dp.callback_query(F.data.startswith("i|"))
async def cb_item(cq: CallbackQuery):
    _, sec, cat, key = cq.data.split("|")
    it = get_item(sec, cat, key)
    if not it:
        return await cq.answer("Topilmadi", show_alert=True)
    await cq.answer("⏳ Yuklanmoqda...")
    await show_item(cq.message, cq.from_user.id, sec, cat, it)


async def _edit_or_send(cq: CallbackQuery, text: str, kb: InlineKeyboardMarkup):
    await cq.answer()
    try:
        await cq.message.edit_text(text, reply_markup=kb)
    except TelegramBadRequest:
        await cq.message.answer(text, reply_markup=kb)


@dp.message(F.text)
async def search(msg: Message):
    q = msg.text.lower().strip()
    if len(q) > 40 or "\n" in q:  # bu qidiruv emas — ehtimol kanal uchun post matni
        if is_admin(msg.from_user.id):
            return await msg.answer("📝 Bu postni kanalga joylash uchun shu xabarga <b>Reply</b> qilib yozing:\n"
                                    "<code>/post quiz-all 🎯 Viktorinani boshlash</code>")
        return await msg.answer("🔎 Qidirish uchun a'zo nomini qisqa yozing, masalan: <i>son suyagi</i>",
                                reply_markup=main_menu())
    if len(q) < 3:
        return await msg.answer("Kamida 3 ta harf yozing 🙂", reply_markup=main_menu())
    hits = [(s, c, i) for s, c, i in all_items()
            if q in i["title"].lower() or q in i["lat"].lower() or q in i["en"].lower()]
    if not hits:
        return await msg.answer("😔 Hech narsa topilmadi. Boshqacha yozib ko'ring yoki bo'limlardan tanlang.",
                                reply_markup=main_menu())
    rows = [[InlineKeyboardButton(text=f"{SECTIONS[s]['title'][:2]} {i['title']}", callback_data=f"i|{s}|{c}|{i['key']}")]
            for s, c, i in hits[:15]]
    rows.append([HOME_IB])
    await msg.answer(f"🔎 <b>{len(hits)}</b> ta natija topildi:", reply_markup=InlineKeyboardMarkup(inline_keyboard=rows))


# ───────────────────────── Ishga tushirish ─────────────────────────

async def main():
    global http
    token = os.getenv("BOT_TOKEN")
    if not token or token.startswith("123456"):
        raise SystemExit("❌ BOT_TOKEN topilmadi. .env faylini yarating va @BotFather bergan tokenni yozing.")
    http = aiohttp.ClientSession(connector=aiohttp.TCPConnector(family=socket.AF_INET))
    bot = Bot(token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    runner = await webserver.start_server()
    tunnel = asyncio.create_task(webserver.run_tunnel())
    try:
        me = await bot.get_me()
        log.info("Bot ishga tushdi: @%s", me.username)
        await dp.start_polling(bot)
    finally:
        tunnel.cancel()
        await runner.cleanup()
        await http.close()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
