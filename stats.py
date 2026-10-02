"""Foydalanuvchilar statistikasi — Upstash Redis (REST) da saqlanadi.

Vercel'da Storage → Upstash Redis ulanganda KV_REST_API_URL / KV_REST_API_TOKEN
(yoki UPSTASH_REDIS_REST_URL / UPSTASH_REDIS_REST_TOKEN) o'zgaruvchilari avtomatik qo'shiladi.
Ular bo'lmasa statistika shunchaki o'chiq — bot odatdagidek ishlayveradi.

Kalitlar:
  users            — barcha foydalanuvchilar (set)
  day:YYYY-MM-DD   — shu kuni faol bo'lganlar (set, 40 kun saqlanadi)
  new:YYYY-MM-DD   — shu kuni birinchi marta kelganlar (son)
  quizzes          — boshlangan viktorinalar (son)
"""

import logging
import os
import re
from datetime import datetime, timedelta, timezone

import aiohttp

log = logging.getLogger("stats")
TZ = timezone(timedelta(hours=5))  # Toshkent vaqti
DAY_TTL = 40 * 24 * 3600


def _cfg() -> tuple[str, str] | None:
    url = os.getenv("KV_REST_API_URL") or os.getenv("UPSTASH_REDIS_REST_URL")
    token = os.getenv("KV_REST_API_TOKEN") or os.getenv("UPSTASH_REDIS_REST_TOKEN")
    return (url.rstrip("/"), token) if url and token else None


def enabled() -> bool:
    return _cfg() is not None


def env_like(*words: str) -> dict[str, str]:
    """Nomida shu so'zlardan biri bor muhit o'zgaruvchilari (ADMIN_IDS, ADMINS_ID, ADMIN_ID ... hammasi)."""
    out = {}
    for k, v in os.environ.items():
        name = re.sub(r"[^A-Z]", "", k.upper())
        if any(w in name for w in words):
            out[k] = v
    return out


def admin_ids() -> set[int]:
    # Nomida ADMIN bor istalgan o'zgaruvchidagi barcha raqamlar — nom va format xatolariga chidamli
    raw = " ".join(env_like("ADMIN").values())
    return {int(x) for x in re.findall(r"\d{5,}", raw)}


def _day(delta: int = 0) -> str:
    return (datetime.now(TZ) - timedelta(days=delta)).strftime("%Y-%m-%d")


async def _pipeline(cmds: list[list]) -> list | None:
    cfg = _cfg()
    if not cfg:
        return None
    url, token = cfg
    try:
        async with aiohttp.ClientSession() as s:
            async with s.post(f"{url}/pipeline", json=cmds, headers={"Authorization": f"Bearer {token}"},
                              timeout=aiohttp.ClientTimeout(total=5)) as r:
                data = await r.json(content_type=None)
        return [x.get("result") for x in data]
    except Exception as e:  # statistika xatosi botni to'xtatmasin
        log.warning("Redis xatosi: %r", e)
        return None


async def track(user_id: int) -> None:
    if not enabled():
        return
    today = _day()
    res = await _pipeline([["SADD", "users", user_id], ["SADD", f"day:{today}", user_id],
                           ["EXPIRE", f"day:{today}", DAY_TTL]])
    if res and res[0] == 1:  # birinchi marta kelgan
        await _pipeline([["INCR", f"new:{today}"], ["EXPIRE", f"new:{today}", DAY_TTL]])


async def quiz_started() -> None:
    if enabled():
        await _pipeline([["INCR", "quizzes"]])


async def report() -> str:
    if not enabled():
        return ("📊 Statistika hali ulanmagan.\n\n"
                "Vercel → loyiha → <b>Storage → Create → Upstash (Redis)</b> ni ulang va Redeploy qiling.")
    days = [_day(i) for i in range(7)]
    res = await _pipeline([["SCARD", "users"], ["SCARD", f"day:{days[0]}"], ["GET", "quizzes"],
                           *[["GET", f"new:{d}"] for d in days],
                           *[["SCARD", f"day:{d}"] for d in days]])
    if not res:
        return "⚠️ Statistikani o'qib bo'lmadi, birozdan keyin urinib ko'ring."
    total, active_today, quizzes = res[0], res[1], int(res[2] or 0)
    new = [int(x or 0) for x in res[3:10]]
    active = res[10:17]
    lines = "\n".join(f"  {d[5:]}: 👤 {a} faol, 🆕 {n} yangi" for d, a, n in zip(days, active, new))
    return (
        "📊 <b>BOT STATISTIKASI</b>\n\n"
        f"👥 Jami foydalanuvchilar: <b>{total}</b>\n"
        f"🔥 Bugun faol: <b>{active_today}</b>\n"
        f"🆕 Bugun yangi: <b>{new[0]}</b>\n"
        f"📅 Shu hafta yangi: <b>{sum(new)}</b>\n"
        f"🎯 Boshlangan viktorinalar: <b>{quizzes}</b>\n\n"
        f"<b>Oxirgi 7 kun:</b>\n{lines}"
    )
