"""Vercel uchun 3D ko'ruvchi ro'yxatini (webapp/data.json) yaratadi.

Kontent yoki data/media.json o'zgarsa qayta ishga tushiring, so'ng commit + push qiling:
    python build_webapp.py
"""

import json

import webserver

out = webserver.WEBAPP_DIR / "data.json"
out.write_text(json.dumps(webserver.build_data(remote_only=True), ensure_ascii=False), encoding="utf-8")
print(f"✓ {out} yozildi")
