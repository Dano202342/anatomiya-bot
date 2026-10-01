from .common import category, item, section

SKIN = section(
    "teri",
    "🧴 Teri, soch va tuklar",
    """
<b>🧴 TERI, SOCH VA TUKLAR</b>

Teri — tanadagi <b>eng katta a'zo</b>.
• Maydoni: <b>1,5–2 m²</b>
• Vazni: tana vaznining <b>~16%</b> i (teri osti yog' qavati bilan)
• Qalinligi: 0,5 mm (qovoqda) dan 4 mm gacha (tovonda)

Soch, tuklar, tirnoqlar, ter va yog' bezlari — terining <b>hosilalari</b>.
Odam tanasida ~<b>5 million</b> soch follikulasi bor (faqat kaft va oyoq tagida yo'q).

Mavzuni tanlang 👇
""",
    [
        category(
            "skin",
            "🧴 Teri tuzilishi",
            "Teri 3 qavatdan iborat: <b>epidermis</b>, <b>derma</b> va <b>gipoderma</b>.",
            [
                item("skinfunc", "Terining vazifalari", "Cutis", "human skin layers",
                     """
<b>Teri 7 ta asosiy vazifani bajaradi:</b>
1. 🛡 <b>Himoya</b> — mikroblar, UF nurlar, mexanik shikastdan
2. 🌡 <b>Termoregulyatsiya</b> — ter ajratish, qon tomirlarni kengaytirish/toraytirish
3. ✋ <b>Sezgi</b> — teginish, bosim, og'riq, issiq-sovuq
4. 💧 <b>Suv yo'qotishni oldini olish</b>
5. ☀️ <b>D vitamini hosil qilish</b> — quyosh nuri ta'sirida
6. 🚮 <b>Ajratish</b> — ter bilan tuzlar, mochevina
7. 🧪 <b>Immunitet</b> — Langerhans hujayralari

💡 Har daqiqada teridan 30–40 ming o'lik hujayra to'kiladi!
""", q="skin layers"),
                item("epidermis", "Epidermis (ust qavat)", "Epidermis", "epidermis",
                     """
<b>Qalinligi:</b> 0,05–1,5 mm. Qon tomirlari <u>yo'q</u>.

<b>5 qavati (pastdan yuqoriga):</b>
1. <b>Bazal qavat</b> — yangi hujayralar bo'linadi, melanotsitlar bor
2. <b>Tikanakli qavat</b> — hujayralar "tikanlar" bilan bog'langan
3. <b>Donador qavat</b> — keratin to'plana boshlaydi
4. <b>Yaltiroq qavat</b> — faqat kaft va oyoq tagida
5. <b>Shox qavat</b> — o'lik, keratinlangan hujayralar; doimo ko'chib turadi

<b>Hujayralari:</b> keratinotsitlar (~90%), melanotsitlar (pigment), Langerhans (immunitet), Merkel (sezgi).

💡 Epidermis har <b>~28 kunda</b> to'liq yangilanadi.
"""),
                item("dermis", "Derma (asl teri)", "Dermis", "dermis",
                     """
<b>Qalinligi:</b> 1–4 mm — terining asosiy qismi.

<b>2 qavati:</b>
• <b>So'rg'ichli qavat</b> — epidermisga botib kiruvchi so'rg'ichlar; barmoq izlari shu yerda hosil bo'ladi
• <b>To'rsimon qavat</b> — zich kollagen va elastin tolalari: terining mustahkamligi va egiluvchanligi

<b>Tarkibida:</b> qon va limfa tomirlari, nerv uchlari, ter va yog' bezlari, soch follikulalari, soch ko'taruvchi muskullar.

💡 Yosh o'tgan sari kollagen kamayadi → ajinlar paydo bo'ladi.
"""),
                item("hypodermis", "Gipoderma (teri osti yog' qavati)", "Tela subcutanea", "subcutaneous tissue",
                     """
<b>Tarkibi:</b> yog' hujayralari (adipotsitlar) va siyrak biriktiruvchi to'qima.

<b>Vazifasi:</b>
• Issiqlikni saqlash (izolyatsiya)
• Energiya zaxirasi
• Zarbalarni yumshatish ("amortizator")
• Terini muskullarga biriktirish

<b>Qalinligi:</b> qovoqda deyarli yo'q, qorin va dumbada bir necha sm gacha.
""", q="hypodermis"),
                item("receptors", "Teri retseptorlari", "Receptores cutanei", "skin receptors",
                     """
<b>Teridagi sezgi retseptorlari:</b>
• <b>Meysner tanachalari</b> — yengil teginish (barmoq uchlarida, lablarda ko'p)
• <b>Pachini tanachalari</b> — chuqur bosim va tebranish
• <b>Merkel disklari</b> — doimiy bosim, shakl va tekstura
• <b>Ruffini tanachalari</b> — teri cho'zilishi
• <b>Erkin nerv uchlari</b> — og'riq, issiq va sovuq

💡 Barmoq uchida 1 sm² da ~100 ta, orqada esa juda kam retseptor bor — shuning uchun barmoqlar eng sezgir.
""", q="pacinian corpuscle"),
                item("glands", "Ter va yog' bezlari", "Glandulae sudoriferae et sebaceae", "sweat gland",
                     """
<b>🔹 Ter bezlari (2–4 million):</b>
• <b>Ekkrin</b> — butun tanada, ayniqsa kaft, oyoq tagi, peshonada; suvli ter → tanani sovutadi.
  Sutkada 0,5 litrdan (tinch holatda) 10 litrgacha (issiq va og'ir ishda) ter ajraladi.
• <b>Apokrin</b> — qo'ltiq osti, chov sohasida; balog'atdan keyin faollashadi; ter hidi bakteriyalar ta'sirida paydo bo'ladi.

<b>🔹 Yog' bezlari:</b>
• Soch follikulasiga ochiladi
• <b>Sebum</b> (teri yog'i) ishlab chiqaradi — teri va sochni yumshatadi, suv o'tkazmaydi
• Kaft va oyoq tagida yo'q
⚠️ Ortiqcha faolligi va tiqilishi — <i>akne (husnbuzar)</i>.
"""),
                item("melanin", "Teri rangi va melanin", "Melaninum", "melanocyte",
                     """
<b>Teri rangini belgilovchi omillar:</b>
• <b>Melanin</b> — melanotsitlar ishlab chiqaradigan pigment (asosiy omil)
• Karotin — sarg'ish tus
• Gemoglobin — qizg'ish/pushti tus

<b>Melanin turlari:</b>
• Eumelanin — qora-jigarrang
• Feomelanin — sariq-qizg'ish

💡 Barcha odamlarda melanotsitlar soni deyarli <b>bir xil</b>! Farq — ular qancha va qanday melanin ishlab chiqarishida.
☀️ Quyoshda qorayish — melaninning ko'payishi, terini UF nurlardan himoya qiladi.
"""),
            ],
        ),
        category(
            "hair",
            "💇 Soch tuzilishi va o'sishi",
            "Soch — keratindan tashkil topgan ipsimon hosila. Boshda ~<b>100 000–150 000</b> ta soch bor.",
            [
                item("hairstruct", "Soch tuzilishi", "Pilus", "hair follicle",
                     """
<b>Soch 2 qismdan iborat:</b>
• <b>Soch o'zagi (stvoli)</b> — teri ustidagi ko'rinadigan qism (o'lik hujayralar)
• <b>Soch ildizi</b> — teri ichidagi qism

<b>Soch o'zagining 3 qavati (kesmada):</b>
1. <b>Kutikula</b> — tashqi, cherepitsadek joylashgan tangachalar (sochga yaltiroqlik beradi)
2. <b>Korteks (po'stloq)</b> — asosiy qism, rang va mustahkamlik beradi
3. <b>Medulla (mag'iz)</b> — markaziy qism (ingichka sochlarda bo'lmasligi mumkin)

💡 Bitta soch tolasi 100 g gacha yukni ko'tara oladi — butun sochlar esa ~12 tonnani!
""", q="hair structure"),
                item("follicle", "Soch follikulasi", "Folliculus pili", "hair follicle anatomy",
                     """
<b>Follikula</b> — soch ildizini o'rab turuvchi xaltacha (dermada joylashgan).

<b>Qismlari:</b>
• <b>Soch piyozchasi</b> — ildizning kengaygan pastki uchi; bu yerda hujayralar tez bo'linadi
• <b>Soch so'rg'ichi</b> — piyozcha ichidagi qon tomirli qism; sochni oziqlantiradi
• <b>Ichki va tashqi ildiz qinlari</b>
• <b>Yog' bezi</b> — follikulaga ochiladi
• <b>Soch ko'taruvchi muskul</b>

💡 Yangi follikulalar tug'ilgandan keyin hosil bo'lmaydi — ularning hammasi ona qornida shakllanadi.
"""),
                item("hairgrowth", "Soch o'sish sikli", "Cyclus pili", "hair growth cycle",
                     """
<b>Har bir soch 3 bosqichdan o'tadi:</b>

🌱 <b>Anagen (o'sish)</b> — 2–7 yil. Sochlarning ~85–90% shu bosqichda.
🍂 <b>Katagen (o'tish)</b> — 2–3 hafta. O'sish to'xtaydi, follikula qisqaradi.
💤 <b>Telogen (dam olish)</b> — ~3 oy. So'ng soch to'kiladi, o'rniga yangisi o'sadi.

<b>Raqamlar:</b>
• O'sish tezligi: oyiga <b>~1–1,5 sm</b> (yiliga ~15 sm)
• Kuniga <b>50–100 ta</b> soch to'kilishi — normal
• Anagen qancha uzoq bo'lsa, soch shuncha uzun o'sadi
""", q="hair cycle"),
                item("haircolor", "Soch rangi va oqarish", "Color pili", "hair color melanin",
                     """
<b>Soch rangi</b> korteksdagi melanin miqdori va turiga bog'liq:
• Ko'p eumelanin → qora, jigarrang
• Kam eumelanin → sariq (blond)
• Feomelanin → malla (qizil)

<b>Oqarish:</b> yosh o'tgan sari piyozchadagi melanotsitlar pigment ishlab chiqarmay qo'yadi va soch ichida havo pufakchalari ko'payadi → soch oq ko'rinadi.

<b>Sochning shakli</b> follikula shakliga bog'liq:
• Yumaloq follikula → to'g'ri soch
• Oval follikula → to'lqinli
• Yassi follikula → jingalak
""", q="human hair"),
            ],
        ),
        category(
            "tuk",
            "🧔 Tuklar va tirnoqlar",
            "Tana tuklari turlari, soch ko'taruvchi muskul va tirnoqlar haqida.",
            [
                item("hairtypes", "Tuk turlari", "Pili", "vellus hair",
                     """
<b>3 xil tuk bor:</b>

👶 <b>Lanugo</b> — ona qornidagi homilada (5-oydan) butun tanani qoplaydigan juda mayin, pigmentsiz tuk. Odatda tug'ilishdan oldin to'kiladi.

🌫 <b>Vellus (mayin tuk)</b> — bolalar va kattalar tanasining ko'p qismida; kalta (2 mm dan kam), ingichka, rangsiz. Ayollar tanasidagi tuklarning ko'pchiligi shu.

🧔 <b>Terminal (dag'al tuk)</b> — uzun, yo'g'on, pigmentli: bosh sochi, qosh, kiprik, balog'atdan keyin — soqol, qo'ltiq osti, chov tuklari.

💡 Balog'at yoshida androgen gormonlar ta'sirida ba'zi vellus tuklar terminal tukka aylanadi.
"""),
                item("brows", "Qosh va kipriklar", "Supercilia et cilia", "eyelashes",
                     """
<b>Qoshlar:</b>
• Ter va yomg'ir suvini ko'zdan chetga oqizadi
• Yuz ifodasi va muloqotda muhim
• ~250 ta tuk, yashash muddati ~4 oy

<b>Kipriklar:</b>
• Ko'zni chang va mayda zarrachalardan himoya qiladi
• Teginishga juda sezgir — ko'zni darhol yumish refleksini qo'zg'atadi
• Yuqori qovoqda 90–160, pastkisida 75–80 ta
• Kiprik follikulasidagi yog' bezlari yallig'lanishi — <i>arpa</i>
""", q="eyebrow"),
                item("arrector", "Soch ko'taruvchi muskul", "M. arrector pili", "arrector pili muscle",
                     """
<b>Joylashuvi:</b> dermada; bir uchi follikulaga, ikkinchisi dermaning so'rg'ichli qavatiga birikadi.
<b>Turi:</b> silliq muskul (ixtiyorsiz), simpatik nerv tizimi boshqaradi.

<b>Vazifasi:</b> qisqarganda tukni tik turg'izadi → <b>"g'oz terisi"</b> (eti junjikishi).
Sabablari: sovuq, qo'rquv, kuchli hayajon.

💡 Hayvonlarda bu issiqlikni saqlaydi va hayvonni kattaroq ko'rsatadi; odamda esa evolyutsion "qoldiq" reaksiya.
Qisqarganda yog' bezini ham siqib, teriga sebum chiqaradi.
"""),
                item("nails", "Tirnoqlar", "Unguis", "nail anatomy",
                     """
<b>Tirnoq</b> — zich keratindan iborat shox plastinka.

<b>Qismlari:</b>
• <b>Tirnoq plastinkasi</b> — ko'rinadigan qattiq qism
• <b>Tirnoq matriksi</b> — ildizdagi o'sish zonasi (shikastlansa tirnoq o'smaydi)
• <b>Lunula</b> — tirnoq asosidagi oq yarim oy
• <b>Kutikula</b> — matriksni infeksiyadan himoya qiluvchi teri chetchasi
• <b>Tirnoq o'rni</b> — plastinka ostidagi pushti teri (qon tomirlari ko'p)

<b>O'sish tezligi:</b>
• Qo'l tirnoqlari — oyiga ~3 mm (to'liq yangilanish ~6 oy)
• Oyoq tirnoqlari — oyiga ~1 mm (12–18 oy)

💡 Tirnoq holati ko'p kasalliklarni ko'rsatadi (kamqonlik, temir yetishmasligi va h.k.).
""", q="fingernail"),
            ],
        ),
    ],
)
