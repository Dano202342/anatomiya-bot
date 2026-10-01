"""3D ko'ruvchi (Telegram Mini App) uchun veb-server va HTTPS tunnel.

Telegram Mini App faqat HTTPS manzilda ochiladi. Uch yo'l bor:
  • Railway — RAILWAY_PUBLIC_DOMAIN avtomatik olinadi
  • .env da WEBAPP_URL=https://... — o'zingizning doimiy hostingingiz (VPS)
  • aks holda bot localhost.run tunnelini Windows'ning o'zidagi ssh orqali ochadi
    (bepul, hech narsa o'rnatish shart emas; manzil vaqti-vaqti bilan o'zgaradi — bot buni kuzatadi)
"""

import asyncio
import logging
import os
import re

from aiohttp import web

import media
from content import SECTIONS

log = logging.getLogger("webapp")
WEBAPP_DIR = media.BASE / "webapp"
# Railway/Render kabi platformalar PORT beradi va tashqaridan shu portga ulanadi
PORT = int(os.getenv("PORT") or os.getenv("WEBAPP_PORT") or "8088")
HOST = "0.0.0.0" if os.getenv("PORT") else "127.0.0.1"


def _fixed_url() -> str | None:
    """Doimiy HTTPS manzil: WEBAPP_URL, Vercel yoki Railway bergan domen."""
    if os.getenv("WEBAPP_URL"):
        return os.getenv("WEBAPP_URL").rstrip("/")
    if os.getenv("VERCEL_PROJECT_PRODUCTION_URL"):  # Vercel'da sahifa statik: /webapp/
        return f"https://{os.getenv('VERCEL_PROJECT_PRODUCTION_URL')}/webapp"
    if os.getenv("RAILWAY_PUBLIC_DOMAIN"):
        return "https://" + os.getenv("RAILWAY_PUBLIC_DOMAIN")
    return None

state: dict = {"url": None}


def public_url() -> str | None:
    return state["url"] or _fixed_url()


def _local(sec: str, key: str, exts: tuple) -> str | None:
    for ext in exts:
        if (media.MEDIA_DIR / sec / f"{key}.{ext}").exists():
            return f"m/{sec}/{key}.{ext}"
    return None


def build_data(remote_only: bool = False) -> dict:
    """3D ko'ruvchi uchun ro'yxat. remote_only=True — Vercel uchun (mahalliy media/ yo'q)."""
    sections = []
    for s in SECTIONS.values():
        items = []
        for c in s["categories"]:
            for it in c["items"]:
                remote = media._cache.get(f"{s['key']}/{it['key']}") or {}
                local_a = None if remote_only else _local(s["key"], it["key"], ("gif",))
                local_p = None if remote_only else _local(s["key"], it["key"], ("jpg", "jpeg", "png", "webp"))
                anim = local_a or (remote.get("anim") or {}).get("url")
                photo = local_p or (remote.get("photo") or {}).get("url")
                items.append({"key": it["key"], "title": it["title"], "lat": it["lat"], "en": it["en"],
                              "anim": anim, "photo": photo})
        sections.append({"key": s["key"], "title": s["title"], "items": items})
    return {"sections": sections}


def has_anim(sec: str, key: str) -> bool:
    return bool(_local(sec, key, ("gif",)) or (media._cache.get(f"{sec}/{key}") or {}).get("anim"))


async def _index(_):
    return web.FileResponse(WEBAPP_DIR / "index.html", headers={"Cache-Control": "no-cache"})


async def _data(_):
    return web.json_response(build_data(), headers={"Cache-Control": "no-cache"})


async def start_server() -> web.AppRunner:
    app = web.Application()
    app.router.add_get("/", _index)
    app.router.add_get("/data.json", _data)
    media.MEDIA_DIR.mkdir(exist_ok=True)
    app.router.add_static("/m/", media.MEDIA_DIR, append_version=False)
    runner = web.AppRunner(app)
    await runner.setup()
    await web.TCPSite(runner, HOST, PORT).start()
    log.info("Veb-server: http://%s:%s", HOST, PORT)
    return runner


async def run_tunnel():
    """localhost.run tunnelini ochadi va uzilsa qayta ulaydi."""
    if _fixed_url():
        state["url"] = _fixed_url()
        log.info("3D ko'ruvchi manzili: %s", state["url"])
        return
    pat = re.compile(r"https://[a-z0-9-]+\.lhr\.life")
    while True:
        try:
            proc = await asyncio.create_subprocess_exec(
                "ssh", "-o", "StrictHostKeyChecking=accept-new", "-o", "ServerAliveInterval=30",
                "-o", "ExitOnForwardFailure=yes", "-R", f"80:127.0.0.1:{PORT}", "nokey@localhost.run",
                stdin=asyncio.subprocess.DEVNULL, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT,
            )
            try:
                async for line in proc.stdout:
                    m = pat.search(line.decode(errors="ignore"))
                    if m and m.group(0) != state["url"]:
                        state["url"] = m.group(0)
                        log.info("3D ko'ruvchi manzili: %s", state["url"])
                await proc.wait()
            finally:
                if proc.returncode is None:  # bot to'xtaganda ssh ham yopilsin
                    proc.kill()
        except FileNotFoundError:
            log.error("ssh topilmadi — 3D ko'ruvchi o'chiq. .env ga WEBAPP_URL yozing.")
            return
        except Exception as e:
            log.warning("Tunnel xatosi: %r", e)
        state["url"] = None
        log.warning("Tunnel uzildi, 5 soniyadan keyin qayta ulanadi")
        await asyncio.sleep(5)
