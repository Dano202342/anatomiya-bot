"""Kontent uchun yordamchi funksiyalar."""


def item(key: str, title: str, lat: str, en: str, text: str, q: str | None = None) -> dict:
    """Bitta mavzu (nerv, muskul, suyak ...).

    key   - qisqa ID (callback_data uchun, 12 belgidan oshmasin)
    title - o'zbekcha nomi
    lat   - lotincha (xalqaro) nomi
    en    - inglizcha nomi: 3D model / video qidirish uchun
    text  - batafsil tushuntirish (HTML)
    q     - Wikimedia Commons'da 3D rasm qidirish so'rovi (bo'lmasa en ishlatiladi)
    """
    return {"key": key, "title": title, "lat": lat, "en": en, "text": text.strip(), "q": q or en}


def category(key: str, title: str, intro: str, items: list[dict]) -> dict:
    return {"key": key, "title": title, "intro": intro.strip(), "items": items}


def section(key: str, title: str, intro: str, categories: list[dict]) -> dict:
    return {"key": key, "title": title, "intro": intro.strip(), "categories": categories}
