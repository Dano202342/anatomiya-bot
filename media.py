"""3D rasm va animatsiyalar.

Manba: Wikimedia Commons. U yerda BodyParts3D / Anatomography loyihasining
haqiqiy 3D modellardan olingan aylanuvchi animatsiyalari (GIF) va 3D renderlari bor
(litsenziya: CC BY-SA). Bot ularni Telegram'ga "animatsiya" (video) va rasm sifatida yuboradi.

Har bir mavzu uchun media ustuvorligi:
  1) media/<bo'lim>/<mavzu>.mp4|.gif  va  .jpg|.png  — o'zingiz qo'ygan fayllar
  2) data/media.json                   — resolve_media.py oldindan topgan havolalar
"""

import asyncio
import json
import logging
from pathlib import Path
from urllib.parse import quote_plus

import aiohttp

BASE = Path(__file__).parent
MEDIA_DIR = BASE / "media"
DATA_DIR = BASE / "data"
MEDIA_JSON = DATA_DIR / "media.json"

API = "https://commons.wikimedia.org/w/api.php"
HEADERS = {"User-Agent": "AnatomiyaUzBot/1.0 (educational Telegram bot)"}
MAX_BYTES = 45 * 1024 * 1024  # Telegram bot API cheklovi 50 MB

log = logging.getLogger(__name__)


def _load() -> dict:
    try:
        return json.loads(MEDIA_JSON.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


_cache: dict = _load()


def _save() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    MEDIA_JSON.write_text(json.dumps(_cache, ensure_ascii=False, indent=1), encoding="utf-8")


def links(item: dict) -> dict:
    """Interaktiv 3D model va video havolalari."""
    en = item["en"]
    return {
        "3d": f"https://sketchfab.com/search?q={quote_plus(en + ' anatomy')}&type=models",
        "video": f"https://www.youtube.com/results?search_query={quote_plus(en + ' 3D anatomy animation')}",
    }


async def get_media(session: aiohttp.ClientSession, sec: str, item: dict) -> dict:
    """{'anim': (manba, nom), 'photo': (manba, nom)} — manba: Path yoki URL."""
    result: dict = {"anim": None, "photo": None}

    # 1) Mahalliy fayllar
    d = MEDIA_DIR / sec
    for ext in ("mp4", "gif"):
        p = d / f"{item['key']}.{ext}"
        if p.exists():
            result["anim"] = (p, p.name)
            break
    for ext in ("jpg", "jpeg", "png", "webp"):
        p = d / f"{item['key']}.{ext}"
        if p.exists():
            result["photo"] = (p, p.name)
            break

    # 2) Oldindan topilgan Commons / Vikipediya havolalari (resolve_media.py)
    found = _cache.get(f"{sec}/{item['key']}") or {}
    for kind in ("anim", "photo"):
        if not result[kind] and found.get(kind):
            result[kind] = (found[kind]["url"], found[kind]["title"])
    return result


async def download(session: aiohttp.ClientSession, url: str, attempts: int = 3, timeout: int = 30) -> bytes | None:
    for n in range(attempts):  # Wikimedia ba'zan ulanishni "osiltirib" qo'yadi — qayta urinamiz
        try:
            # sock_read: ma'lumot oqib turgan bo'lsa katta fayl ham uzilmaydi
            t = aiohttp.ClientTimeout(total=timeout * 4, sock_connect=15, sock_read=timeout)
            async with session.get(url, headers=HEADERS, timeout=t) as r:
                if r.status == 200:
                    data = await r.read()
                    return data if len(data) < MAX_BYTES else None
                log.warning("Yuklab bo'lmadi %s: HTTP %s", url, r.status)
                if r.status not in (429, 500, 502, 503, 504):
                    return None
        except Exception as e:
            log.warning("Yuklab bo'lmadi (%d-urinish) %s: %r", n + 1, url, e)
        await asyncio.sleep(2 + n * 3)
    return None
