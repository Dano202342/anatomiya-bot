"""🎯 Viktorina — 10 ta savol, 4 ta variant.

Holat serverda saqlanmaydi (Vercel har so'rovda yangidan ishga tushadi): bo'lim, savol raqami va ball
har bir tugmaning callback_data'sida yuradi:
    q|<filtr>|<n>|<ball>|<bo'lim>|<to'g'ri_kalit>|<tanlangan_kalit>
"""

import logging
import random

from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

import media
from content import SECTIONS, all_items

log = logging.getLogger("quiz")
router = Router()

TOTAL = 10
SKIP_CATS = {"general"}          # umumiy nazariy mavzular savolga yaramaydi
SKIP_ITEMS = {"skinfunc", "receptors"}

# (bo'lim, kalit) -> (kategoriya, mavzu)
INDEX = {(s, i["key"]): (c, i) for s, c, i in all_items()}
POOL = [(s, c, i) for s, c, i in all_items() if c not in SKIP_CATS and i["key"] not in SKIP_ITEMS]

HOME = InlineKeyboardButton(text="🏠 Bosh menyu", callback_data="home")


def menu_kb() -> InlineKeyboardMarkup:
    rows = [[InlineKeyboardButton(text="🎲 Aralash — barcha bo'limlar", callback_data="qs|all")]]
    rows += [[InlineKeyboardButton(text=s["title"], callback_data=f"qs|{k}")] for k, s in SECTIONS.items()]
    rows.append([HOME])
    return InlineKeyboardMarkup(inline_keyboard=rows)


MENU_TEXT = """
🎯 <b>VIKTORINA</b>

Bilimingizni sinab ko'ring! <b>10 ta savol</b>, har birida 4 ta javob varianti.

Savol turlari:
🧊 3D model yoki rasmga qarab a'zoni topish
🏷 Lotincha nomdan o'zbekcha nomini topish (va aksincha)

Mavzuni tanlang 👇
"""


async def send_menu(msg: Message):
    await msg.answer(MENU_TEXT, reply_markup=menu_kb())


def _pool(flt: str):
    return [x for x in POOL if flt == "all" or x[0] == flt]


def _options(sec: str, cat: str, correct: dict) -> list[dict]:
    """To'g'ri javob + 3 ta chalg'ituvchi (iloji boricha shu kategoriyadan — qiyinroq)."""
    same_cat = [i for s, c, i in POOL if s == sec and c == cat and i["key"] != correct["key"]]
    same_sec = [i for s, c, i in POOL if s == sec and c != cat]
    others = [i for s, c, i in POOL if s != sec]
    random.shuffle(same_cat), random.shuffle(same_sec), random.shuffle(others)
    picked, seen = [], {correct["title"]}
    for i in same_cat + same_sec + others:
        if i["title"] not in seen:
            picked.append(i)
            seen.add(i["title"])
        if len(picked) == 3:
            break
    opts = picked + [correct]
    random.shuffle(opts)
    return opts


def _short(title: str) -> str:
    return title if len(title) <= 40 else title[:38] + "…"


async def ask(msg: Message, flt: str, n: int, score: int):
    """n — shu paytgacha javob berilgan savollar soni."""
    sec, cat, it = random.choice(_pool(flt))
    m = media._cache.get(f"{sec}/{it['key']}") or {}
    has_media = bool(m.get("anim") or m.get("photo"))
    mode = random.choice(["media", "media", "lat", "uz"] if has_media else ["lat", "uz"])
    opts = _options(sec, cat, it)

    def cb(o):
        return f"q|{flt}|{n}|{score}|{sec}|{it['key']}|{o['key']}"

    head = f"🎯 <b>Savol {n + 1}/{TOTAL}</b>   ⭐️ Ball: {score}\n\n"
    if mode == "uz":
        q = head + f"<b>{it['title']}</b> — lotincha (xalqaro) nomi qaysi?"
        labels = [o["lat"] for o in opts]
    elif mode == "lat":
        q = head + f"🏷 <b><i>{it['lat']}</i></b>\n\nBu qaysi a'zo / tuzilma?"
        labels = [o["title"] for o in opts]
    else:
        hint = " (3D modelda — rangli qism)" if m.get("anim") else ""
        q = head + f"🔎 Bu qaysi a'zo / tuzilma?{hint}"
        labels = [o["title"] for o in opts]
    kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_short(l), callback_data=cb(o))]
                                               for o, l in zip(opts, labels)])
    if mode == "media":
        for kind in ("anim", "photo"):
            if m.get(kind):
                try:
                    send = msg.answer_animation if kind == "anim" else msg.answer_photo
                    return await send(m[kind]["url"], caption=q, reply_markup=kb)
                except TelegramBadRequest as e:
                    log.warning("Viktorina media yuborilmadi: %s", e)
        q = head + f"🏷 <b><i>{it['lat']}</i></b>\n\nBu qaysi a'zo / tuzilma?"  # media ishlamasa — matnli savol
        kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=_short(o["title"]), callback_data=cb(o))]
                                                   for o in opts])
    await msg.answer(q, reply_markup=kb)


def _grade(score: int) -> str:
    p = score / TOTAL
    if p == 1:
        return "🏆 A'lo! Mukammal natija — siz haqiqiy anatom ekansiz!"
    if p >= 0.8:
        return "🥇 Juda yaxshi! Bilimingiz mustahkam."
    if p >= 0.6:
        return "🥈 Yaxshi! Yana biroz takrorlasangiz, a'lo bo'ladi."
    if p >= 0.4:
        return "🥉 Yomon emas. Bo'limlarni yana bir bor ko'rib chiqing."
    return "📚 Mashq qilish kerak. Bo'limlarni o'qib, qayta urinib ko'ring!"


@router.callback_query(F.data == "qm")
async def cb_menu(cq: CallbackQuery):
    await cq.answer()
    await send_menu(cq.message)


@router.callback_query(F.data.startswith("qs|"))
async def cb_start(cq: CallbackQuery):
    flt = cq.data.split("|")[1]
    if flt != "all" and flt not in SECTIONS:
        return await cq.answer("Topilmadi", show_alert=True)
    await cq.answer("🎯 Boshladik!")
    await ask(cq.message, flt, 0, 0)


@router.callback_query(F.data.startswith("qn|"))
async def cb_next(cq: CallbackQuery):
    _, flt, n, score = cq.data.split("|")
    await cq.answer()
    await ask(cq.message, flt, int(n), int(score))


@router.callback_query(F.data.startswith("q|"))
async def cb_answer(cq: CallbackQuery):
    _, flt, n, score, sec, right, chosen = cq.data.split("|")
    n, score = int(n) + 1, int(score)
    found = INDEX.get((sec, right))
    if not found:
        return await cq.answer("Savol eskirgan, yangisini boshlang", show_alert=True)
    cat, it = found
    ok = chosen == right
    score += ok
    await cq.answer("✅ To'g'ri!" if ok else "❌ Noto'g'ri")

    verdict = ("✅ <b>To'g'ri!</b>" if ok else
               f"❌ <b>Noto'g'ri.</b>\nTo'g'ri javob: <b>{it['title']}</b>")
    text = (f"🎯 <b>Savol {n}/{TOTAL}</b>   ⭐️ Ball: {score}\n\n{verdict}\n"
            f"🏷 <i>{it['lat']}</i>")
    rows = [[InlineKeyboardButton(text="📖 Batafsil o'qish", callback_data=f"i|{sec}|{cat}|{it['key']}")]]
    if n < TOTAL:
        rows.insert(0, [InlineKeyboardButton(text="Keyingi savol ➡️", callback_data=f"qn|{flt}|{n}|{score}")])
    kb = InlineKeyboardMarkup(inline_keyboard=rows)

    # Savol xabarini natija bilan almashtiramiz (qayta bosib ball yig'ib bo'lmasin)
    try:
        if cq.message.text:
            await cq.message.edit_text(text, reply_markup=kb)
        else:
            await cq.message.edit_caption(caption=text, reply_markup=kb)
    except TelegramBadRequest:
        await cq.message.answer(text, reply_markup=kb)

    if n >= TOTAL:
        await cq.message.answer(
            f"🏁 <b>Viktorina tugadi!</b>\n\nNatija: <b>{score} / {TOTAL}</b>\n{_grade(score)}",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🔄 Qayta o'ynash", callback_data=f"qs|{flt}")],
                [InlineKeyboardButton(text="🎯 Boshqa mavzu", callback_data="qm"), HOME],
            ]))
