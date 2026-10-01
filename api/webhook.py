"""Vercel serverless funksiyasi: Telegram har bir yangilanishni shu manzilga POST qiladi.

Manzil: https://<loyiha>.vercel.app/api/webhook
Vercel muhit o'zgaruvchilari: BOT_TOKEN, WEBHOOK_SECRET
"""

import asyncio
import json
import os
import socket
import sys
from http.server import BaseHTTPRequestHandler
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import aiohttp  # noqa: E402
from aiogram import Bot  # noqa: E402
from aiogram.client.default import DefaultBotProperties  # noqa: E402
from aiogram.enums import ParseMode  # noqa: E402
from aiogram.types import Update  # noqa: E402

import bot as app  # noqa: E402


async def process(data: dict) -> None:
    tg = Bot(os.environ["BOT_TOKEN"], default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    app.http = aiohttp.ClientSession(connector=aiohttp.TCPConnector(family=socket.AF_INET))
    try:
        await app.dp.feed_update(tg, Update.model_validate(data, context={"bot": tg}))
    finally:
        await app.http.close()
        await tg.session.close()


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        secret = os.getenv("WEBHOOK_SECRET")
        if secret and self.headers.get("X-Telegram-Bot-Api-Secret-Token") != secret:
            self.send_response(403)
            self.end_headers()
            return
        body = self.rfile.read(int(self.headers.get("Content-Length") or 0))
        try:
            asyncio.run(process(json.loads(body)))
        except Exception as e:  # Telegram qayta-qayta yubormasligi uchun baribir 200 qaytaramiz
            app.log.exception("Yangilanishni qayta ishlashda xato: %r", e)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"ok")

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("Anatomiya boti ishlayapti ✅".encode())
