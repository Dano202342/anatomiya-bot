# 🧬 Anatomiya boti (Telegram)

Odam tanasini **3D animatsiyalar, 3D tasvirlar va video darslar** bilan o'zbek tilida o'rgatuvchi bot.

## Bo'limlar
| Tugma | Ichida |
|---|---|
| 🧠 Nerv tizimi | Neyron, MNT, **12 juft bosh miya nervi** (har biri alohida), orqa miya nervlari va chigallar, qo'l va oyoq nervlari, vegetativ tizim |
| 💪 Muskullar | Bosh, bo'yin, ko'krak, qorin, orqa, yelka, bilak-kaft, chanoq-son, boldir-panja muskullari |
| 🧴 Teri, soch va tuklar | Teri qavatlari, retseptorlar, bezlar, melanin, soch tuzilishi va o'sish sikli, tuk turlari, tirnoqlar |
| 🦴 Suyaklar | 206 suyak: nomi, qayerda, nechta, qaysi bo'g'imlar; asosiy bo'g'imlar (tizza, yelka, tirsak, son-chanoq) |

Har bir mavzuda bot yuboradi:
- 🧊 **aylanuvchi 3D animatsiya** (BodyParts3D haqiqiy 3D modelidan, Wikimedia Commons)
- 🖼 **3D tasvir**
- 📖 batafsil matn
- 🔗 **interaktiv 3D model** (Sketchfab — barmoq bilan aylantirish) va **3D video darslar** (YouTube)

Shuningdek, istalgan nomni yozib **qidirish** mumkin (o'zbekcha, lotincha, inglizcha).

## O'rnatish
1. Telegram'da [@BotFather](https://t.me/BotFather) → `/newbot` → token oling.
2. `.env.example` faylini `.env` deb nusxalang va tokenni yozing.
3. Kutubxonalarni o'rnating va ishga tushiring:
```bash
pip install -r requirements.txt
```
```bash
python bot.py
```

`data/media.json` tayyor holda keladi (69 ta 3D animatsiya, 145 ta rasm). Bot har bir faylni birinchi marta
Wikimedia'dan yuklab yuboradi, keyin Telegram `file_id` orqali bir zumda yuboradi.
Internet sekin bo'lsa, hammasini oldindan yuklab oling (~150 MB):
```bash
python resolve_media.py --download
```

## O'z rasm/videolaringizni qo'shish
`media/<bo'lim>/<mavzu_kaliti>.<kengaytma>` ko'rinishida fayl qo'ying — bot avval shuni yuboradi:
- video/animatsiya: `.mp4` yoki `.gif`
- rasm: `.jpg`, `.png`, `.webp`

Bo'lim kalitlari: `nerv`, `musk`, `teri`, `suyak`. Mavzu kalitlari `content/*.py` fayllaridagi `item("kalit", ...)` dagi birinchi so'z.
Masalan: `media/suyak/femur.mp4`, `media/nerv/cn7.jpg`.

## Fayllar
- `bot.py` — bot logikasi (menyu, tugmalar, qidiruv)
- `content/` — barcha o'quv matnlari (yangi mavzu qo'shish oson)
- `media.py` — 3D media topish va yuborish
- `resolve_media.py` — barcha mavzular uchun Commons'dan 3D media'ni oldindan topib `data/media.json` ga yozadi
- `data/media.json` — topilgan havolalar (qo'lda tahrirlash mumkin)

3D tasvirlar: Wikimedia Commons / BodyParts3D (DBCLS), CC BY-SA litsenziyasi.
