"""Barcha mavzular uchun 3D animatsiya va 3D rasmlarni topib, data/media.json ga yozadi.

Commons qidiruvi tez cheklanadi (HTTP 429), shuning uchun qidiruv ishlatilmaydi:
  1) Animatsiyalar — "Animations from Anatomography" kategoriyasi (BodyParts3D 3D modellari)
     bir necha so'rovda to'liq yuklanadi va nomlar bo'yicha moslashtiriladi.
  2) Rasmlar — har bir mavzuning ingliz Vikipediya maqolasidagi asosiy rasm
     (50 tadan to'plab so'raladi).

Ishlatish:  python resolve_media.py              — havolalarni topish
            python resolve_media.py --download   — + hamma fayllarni media/ ga yuklab olish (~150 MB)
Natijani data/media.json da qo'lda tuzatish mumkin.
"""

import asyncio
import json
import re
import socket
import sys

import aiohttp

import media
from content import all_items

COMMONS = media.API
WIKI = "https://en.wikipedia.org/w/api.php"
ROOT_CAT = "Category:Animations from Anatomography"
ANIMS_JSON = media.DATA_DIR / "commons_anims.json"

# Kalit -> animatsiya fayl nomida bo'lishi kerak bo'lgan so'zlar (bo'lmasa q dan olinadi)
ANIM_HINTS = {
    "cerebrum": ["cerebrum - frontal lobe"], "cerebellum": ["cerebellum"], "brainstem": ["brainstem", "brain stem"],
    "zygomatic": ["zygomaticus major"], "zygomatic_b": ["zygomatic bone"], "temporal": ["temporal bone"],
    "temporalis": ["temporalis"], "frontal": ["frontal bone"], "occipital": ["occipital bone"],
    "parietal": ["parietal bone"], "mandible": ["mandible"],
    "nasal": ["nasal bone"], "radius": ["radius"], "ribs": ["rib"], "hyoidb": ["hyoid"],
    "ossicles": ["ossicle", "malleus", "incus", "stapes"], "sacrum": ["sacrum", "coccyx"],
    "cervical": ["cervical vertebrae", "atlas"], "thoracic": ["thoracic vertebrae"],
    "lumbar": ["lumbar vertebrae"], "vertebra": ["thoracic vertebrae"],
    "hipbone": ["hip bone"], "carpals": ["carpus"], "tarsals": ["tarsal bones"],
    "metacarpals": ["metacarpal bones"], "metatarsals": ["metatarsal bones", "phalanges of the foot"],
    "knee": [], "hipjoint": ["hip bone"], "shoulder": [], "elbow": [],
    "rotcuff": ["supraspinatus", "infraspinatus"], "hamstrings": ["biceps femoris", "semitendinosus"],
    "glutmed": ["gluteus medius"], "pterygoid": ["medial pterygoid", "lateral pterygoid"], "scalene": ["scalenus anterior"],
    "hyoid": [], "flexors": [], "extensors": [], "handm": [],
    "footm": ["extensor digitorum brevis"], "achilles": ["triceps surae"],
    "fibularis": ["fibularis longus", "peroneus longus"], "adductors": ["adductor longus", "adductor"],
    "intercostm": ["external intercostal"], "erector": [],
    "rhomboid": ["rhomboid"], "frontalis": ["frontalis"],
    "orboculi": [], "ororis": [], "rectusabd": [], "extobl": [], "intobl": [], "transvabd": [],
    # Buyrak, qon aylanish, bezlar: Anatomography'da faqat miyadagi bezlar animatsiyasi bor
    "hypothal": ["hypothalamus"], "pineal": ["pineal"], "pituitary": ["pituitary", "hypophysis"],
    **{k: [] for k in ("kidney nephron ureter bladder urethra ckd stones pyelo glomerulo cystitis heart valves "
                       "conduction coronary aorta veins capillary blood hypertension athero infarct stroke anemia "
                       "heartfail thyroid parathyroid adrenal pancreas gonads thymus diabetes goiter graves "
                       "hypothyroid growthdis cushing").split()},
    "glutmax": ["gluteus maximus"], "quadriceps": ["quadriceps", "rectus femoris", "vastus"],
    "diaphragm": ["diaphragm"], "iliopsoas": ["iliopsoas", "psoas"], "scm": ["sternocleidomastoid"],
}

# Vikipediya maqola nomi (en dan farq qilsa)
WIKI_TITLES = {
    "neuron": "Neuron", "myelin": "Myelin", "skinfunc": "Human skin", "hairstruct": "Hair",
    "follicle": "Hair follicle", "hairgrowth": "Hair follicle", "haircolor": "Human hair color",
    "hairtypes": "Vellus hair", "brows": "Eyelash", "nails": "Nail (anatomy)", "glands": "Sweat gland",
    "melanin": "Melanocyte", "receptors": "Mechanoreceptor", "hypodermis": "Subcutaneous tissue",
    "blood": "Blood cell", "conduction": "Electrical conduction system of the heart", "valves": "Heart valve",
    "graves": "Graves' disease", "cushing": "Cushing's syndrome", "stones": "Kidney stone disease",
    "growthdis": "Acromegaly", "ckd": "Kidney failure", "gonads": "Ovary", "diabetes": "Pancreatic islets",
    "hypothyroid": "Thyroid",
    "bonestruct": "Long bone", "bonetypes": "Long bone", "patella": "Patella", "knee": "Knee",
    "extensors": "Extensor carpi radialis longus muscle", "arrector": "Arrector pili muscle",
    "receptors": "Pacinian corpuscle", "fibular": "Common peroneal nerve", "sartorius": "Sartorius muscle", "jointtypes": "Synovial joint", "ribs": "Rib cage",
    "ossicles": "Ossicles", "gluteal": "Superior gluteal nerve", "flexors": "Flexor digitorum superficialis muscle",
    "extensors": "Extensor digitorum muscle", "handm": "Thenar eminence", "footm": "Flexor digitorum brevis muscle",
    "hamstrings": "Hamstring", "adductors": "Adductor longus muscle", "rotcuff": "Rotator cuff",
    "hyoid": "Suprahyoid muscles", "scalene": "Scalene muscles", "pterygoid": "Lateral pterygoid muscle",
    "intercostm": "Intercostal muscle", "diaphragm": "Thoracic diaphragm", "radius": "Radius (bone)",
    "temporal": "Temporal bone", "frontal": "Frontal bone", "vertebra": "Vertebra", "sacrum": "Sacrum",
    "sympathetic": "Sympathetic trunk", "parasympathetic": "Parasympathetic nervous system",
    "metacarpals": "Metacarpal bones", "metatarsals": "Metatarsal bones", "zygomatic": "Zygomaticus major muscle",
    "fibularis": "Fibularis longus", "achilles": "Achilles tendon",
}


async def _get(session, url, params):
    # Wikimedia bitta ulanishdagi ketma-ket so'rovlarni 429 bilan to'xtatadi — har safar yangi ulanish
    for attempt in range(6):
        await asyncio.sleep(1.5 + attempt * 5)
        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(force_close=True, family=socket.AF_INET),
                                             timeout=aiohttp.ClientTimeout(total=40)) as s:
                async with s.get(url, params={**params, "format": "json"}, headers=media.HEADERS) as r:
                    if r.status == 200:
                        return await r.json(content_type=None)
                    print(f"  HTTP {r.status}, kutyapman...")
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            print(f"  tarmoq xatosi ({e!r}), qayta urinaman...")
    raise RuntimeError("API javob bermadi")


async def collect_anims(session) -> list[str]:
    if ANIMS_JSON.exists():
        return json.loads(ANIMS_JSON.read_text(encoding="utf-8"))
    files, seen, queue = set(), set(), [ROOT_CAT]
    while queue:
        cat = queue.pop()
        if cat in seen:
            continue
        seen.add(cat)
        cont = {}
        while True:
            d = await _get(session, COMMONS, {"action": "query", "list": "categorymembers", "cmtitle": cat,
                                              "cmlimit": "500", "cmtype": "file|subcat", **cont})
            for m in d["query"]["categorymembers"]:
                (queue.append if m["ns"] == 14 else files.add)(m["title"])
            if "continue" not in d:
                break
            cont = d["continue"]
        print(f"  {cat}: jami {len(files)} fayl")
    out = sorted(t.removeprefix("File:") for t in files if t.lower().endswith(".gif"))
    media.DATA_DIR.mkdir(exist_ok=True)
    ANIMS_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=0), encoding="utf-8")
    return out


def match_anim(it: dict, anims: list[str]) -> str | None:
    hints = ANIM_HINTS.get(it["key"])
    if hints is None:
        hints = [it["q"].lower().removesuffix(" muscle").removesuffix(" bone")]
    for h in hints:  # bo'sh ro'yxat = mos animatsiya yo'q
        h = h.lower()
        pat = re.compile(r"\b" + re.escape(h))
        cands = [a for a in anims if pat.search(a.lower())]
        if cands:
            # Nomi aynan shu so'z bilan boshlanadigani ("Femur - animation.gif"), "small" bo'lmagani, eng qisqasi
            def rank(a: str):
                t = a.lower().removeprefix("rotation ").removeprefix("left ")
                return (not t.startswith(h), "small" in t, "close" in t, len(a))
            return min(cands, key=rank)
    return None


async def file_urls(session, titles: list[str]) -> dict:
    out = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        d = await _get(session, COMMONS, {"action": "query", "prop": "imageinfo", "iiprop": "url|size",
                                          "titles": "|".join("File:" + t for t in chunk)})
        for p in d["query"]["pages"].values():
            info = (p.get("imageinfo") or [{}])[0]
            if info.get("url") and info.get("size", 0) < media.MAX_BYTES:
                out[p["title"].removeprefix("File:")] = info["url"]
    return out


async def wiki_images(session, titles: list[str]) -> dict:
    out = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        d = await _get(session, WIKI, {"action": "query", "prop": "pageimages", "piprop": "thumbnail|name",
                                       "pithumbsize": "900", "redirects": "1", "titles": "|".join(chunk)})
        q = d["query"]
        back = {}
        for n in q.get("normalized", []) + q.get("redirects", []):
            back[n["to"]] = back.get(n["from"], n["from"])
        for p in q["pages"].values():
            if "thumbnail" in p:
                src = p["title"]
                while src in back:
                    src = back[src]
                out[src] = {"url": p["thumbnail"]["source"], "title": p.get("pageimage", p["title"])}
                out[p["title"]] = out[src]
    return out


async def main():
    items = list(all_items())
    async with aiohttp.ClientSession() as s:
        print("1) 3D animatsiyalar ro'yxati yuklanmoqda...")
        anims = await collect_anims(s)
        print(f"   {len(anims)} ta animatsiya topildi")

        chosen = {it["key"]: match_anim(it, anims) for _, _, it in items}
        urls = await file_urls(s, sorted({a for a in chosen.values() if a}))

        print("2) Vikipediya rasmlari yuklanmoqda...")
        wt = {it["key"]: WIKI_TITLES.get(it["key"]) or it["en"][0].upper() + it["en"][1:] for _, _, it in items}
        imgs = await wiki_images(s, sorted(set(wt.values())))

    result = {}
    for sec, _, it in items:
        a = chosen[it["key"]]
        anim = {"url": urls[a], "title": a} if a in urls else None
        photo = imgs.get(wt[it["key"]])
        result[f"{sec}/{it['key']}"] = {"anim": anim, "photo": photo}
        print(f"{sec}/{it['key']:14} | 🎞 {(a or '—')[:42]:42} | 🖼 {(photo or {}).get('title', '—')[:45]}")
    media._cache.clear()
    media._cache.update(result)
    media._save()
    na = sum(1 for v in result.values() if v["anim"])
    np_ = sum(1 for v in result.values() if v["photo"])
    print(f"\nTayyor: {len(result)} mavzu, {na} ta 3D animatsiya, {np_} ta rasm → {media.MEDIA_JSON}")

    if "--download" in sys.argv:
        await download_all(result)


async def download_all(result: dict):
    """Hamma media'ni media/<bo'lim>/ papkasiga yuklab oladi — bot internetga bog'liq bo'lmaydi."""
    print("\n3) Fayllar media/ papkasiga yuklanmoqda...")
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(family=socket.AF_INET)) as s:
        for key, m in result.items():
            sec, name = key.split("/")
            for kind in ("anim", "photo"):
                if not m[kind]:
                    continue
                ext = "gif" if kind == "anim" else (m[kind]["url"].split("?")[0].rsplit(".", 1)[-1].lower())
                if ext not in ("gif", "jpg", "jpeg", "png", "webp"):
                    ext = "jpg"
                if kind == "photo" and ext == "gif":
                    continue  # rasm sifatida GIF yaramaydi
                path = media.MEDIA_DIR / sec / f"{name}.{ext}"
                if path.exists():
                    continue
                data = await media.download(s, m[kind]["url"])
                if data:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.write_bytes(data)
                    print(f"  ✓ {path.relative_to(media.BASE)} ({len(data) // 1024} KB)")


if __name__ == "__main__":
    asyncio.run(main())
