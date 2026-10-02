"""Vercel kirish nuqtasi (ASGI ilova, qo'shimcha kutubxonasiz).

Yo'llar:
  POST /api/webhook   — Telegram yangilanishlari (setWebhook shu manzilga qilinadi)
  GET  /webapp/...    — bot ichidagi 3D ko'ruvchi (Telegram Mini App)
  GET  /              — holat sahifasi

Vercel muhit o'zgaruvchilari: BOT_TOKEN, WEBHOOK_SECRET
"""

import json
import os
import socket

import aiohttp
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Update

import bot as tgbot
import webserver

WEBAPP_FILES = {
    "data.json": ("application/json", webserver.WEBAPP_DIR / "data.json"),
    "": ("text/html; charset=utf-8", webserver.WEBAPP_DIR / "index.html"),
}


async def process_update(data: dict) -> None:
    tg = Bot(os.environ["BOT_TOKEN"], default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    tgbot.http = aiohttp.ClientSession(connector=aiohttp.TCPConnector(family=socket.AF_INET))
    try:
        await tgbot.dp.feed_update(tg, Update.model_validate(data, context={"bot": tg}))
    finally:
        await tgbot.http.close()
        await tg.session.close()


async def _respond(send, status: int, body: bytes, ctype: str = "text/plain; charset=utf-8", cache: bool = False):
    headers = [(b"content-type", ctype.encode())]
    if cache:
        headers.append((b"cache-control", b"public, max-age=300"))
    await send({"type": "http.response.start", "status": status, "headers": headers})
    await send({"type": "http.response.body", "body": body})


async def _read_body(receive) -> bytes:
    body = b""
    while True:
        msg = await receive()
        body += msg.get("body", b"")
        if not msg.get("more_body"):
            return body


async def app(scope, receive, send):
    if scope["type"] == "lifespan":
        while True:
            msg = await receive()
            if msg["type"] == "lifespan.startup":
                await send({"type": "lifespan.startup.complete"})
            elif msg["type"] == "lifespan.shutdown":
                await send({"type": "lifespan.shutdown.complete"})
                return
    if scope["type"] != "http":
        return

    path, method = scope["path"], scope["method"]

    if path.rstrip("/") == "/api/webhook" and method == "POST":
        headers = {k.decode().lower(): v.decode() for k, v in scope["headers"]}
        secret = os.getenv("WEBHOOK_SECRET")
        if secret and headers.get("x-telegram-bot-api-secret-token") != secret:
            return await _respond(send, 403, b"forbidden")
        try:
            await process_update(json.loads(await _read_body(receive)))
        except Exception as e:  # Telegram qayta-qayta yubormasligi uchun baribir 200
            tgbot.log.exception("Yangilanishni qayta ishlashda xato: %r", e)
        return await _respond(send, 200, b"ok")

    if path == "/webapp":
        await send({"type": "http.response.start", "status": 301, "headers": [(b"location", b"/webapp/")]})
        return await send({"type": "http.response.body", "body": b""})
    if path.startswith("/webapp/"):
        name = path.removeprefix("/webapp/")
        ctype, file = WEBAPP_FILES.get(name, WEBAPP_FILES[""])
        return await _respond(send, 200, file.read_bytes(), ctype, cache=True)

    ver = (os.getenv("VERCEL_GIT_COMMIT_SHA") or "lokal")[:7]
    admins = "bor" if os.getenv("ADMIN_IDS") else "yo'q"
    return await _respond(send, 200, f"Anatomiya boti ishlayapti ✅\nVersiya: {ver}\nADMIN_IDS: {admins}".encode())
