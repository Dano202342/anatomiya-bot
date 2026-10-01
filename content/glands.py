from .common import category, item, section

GLANDS = section(
    "bez",
    "🧪 Bezlar va gormonlar",
    """
<b>🧪 ENDOKRIN (ICHKI SEKRETSIYA) TIZIMI</b>

<b>Ichki sekretsiya bezlari</b> — yo'li yo'q bezlar; ular <b>gormonlarni</b> to'g'ridan-to'g'ri qonga chiqaradi.
Gormonlar — kimyoviy "xabarchilar": o'sish, moddalar almashinuvi, jinsiy rivojlanish, stressga javob va boshqalarni boshqaradi.

<b>Asosiy bezlar:</b> gipotalamus, gipofiz, epifiz, qalqonsimon bez, qalqonsimon bez oldi bezlari, buyrak usti bezlari, oshqozon osti bezi (orolchalar), jinsiy bezlar.

💡 <b>Qoida:</b> gormon <u>ko'p</u> ishlab chiqarilsa — bir kasallik, <u>kam</u> bo'lsa — boshqa kasallik kelib chiqadi.
Har bir bez haqidagi ma'lumotda ikkalasi ham yozilgan 👇
""",
    [
        category(
            "brain",
            "🧠 Miyadagi bezlar",
            "Gipotalamus, gipofiz va epifiz — endokrin tizimning \"boshqaruv markazi\".",
            [
                item("hypothal", "Gipotalamus", "Hypothalamus", "hypothalamus",
                     """
<b>Joylashuvi:</b> oraliq miyada, gipofiz ustida. Vazni ~4 g.
<b>Vazifasi:</b> nerv va endokrin tizimlarni bog'laydi — <b>gipofizni boshqaradi</b>.

<b>Gormonlari:</b>
• <b>Liberinlar va statinlar</b> — gipofiz gormonlarini ko'paytiradi/kamaytiradi
• <b>ADG (vazopressin)</b> — buyrakda suvni ushlab qoladi
• <b>Oksitotsin</b> — tug'ruqda bachadonni qisqartiradi, sut ajralishi

Shuningdek, tana harorati, ochlik, chanqoq, uyqu markazlari shu yerda.

⚠️ <b>Buzilsa:</b> ADG kam — <i>qandsiz diabet</i> (sutkasiga 5–20 litr siydik, kuchli chanqoq); semizlik, harorat buzilishi.
"""),
                item("pituitary", "Gipofiz", "Hypophysis", "pituitary gland",
                     """
<b>Joylashuvi:</b> ponasimon suyakning turk egarida. No'xatdek, vazni ~0,5 g.
<b>"Bezlar qiroli"</b> — boshqa bezlarni boshqaradi.

<b>Oldingi bo'lak gormonlari:</b>
• <b>O'sish gormoni (STG)</b> — suyak va muskullar o'sishi
• <b>TTG</b> — qalqonsimon bezni boshqaradi
• <b>AKTG</b> — buyrak usti bezini boshqaradi
• <b>FSG, LG</b> — jinsiy bezlarni boshqaradi
• <b>Prolaktin</b> — sut ishlab chiqarish

<b>Orqa bo'lak:</b> gipotalamusdan kelgan ADG va oksitotsinni saqlaydi va chiqaradi.

⚠️ <b>Buzilsa:</b>
• O'sish gormoni bolalikda <b>ko'p</b> — <i>gigantizm</i> (2 m dan baland); kattalarda — <i>akromegaliya</i> (qo'l, oyoq, burun, jag' kattalashadi)
• Bolalikda <b>kam</b> — <i>gipofizar pakanalik (nanizm)</i> — bo'y past, lekin aql normal
"""),
                item("pineal", "Epifiz (shishsimon bez)", "Glandula pinealis", "pineal gland",
                     """
<b>Joylashuvi:</b> miya markazida, o'rta miya ustida. Qarag'ay yong'og'idek, ~0,2 g.

<b>Gormoni:</b> <b>melatonin</b> — "uyqu gormoni". Qorong'ida ko'payadi, yorug'da kamayadi.
<b>Vazifasi:</b> sutkalik ritm (uyqu-bedorlik), jinsiy yetilishni vaqtida boshlash.

⚠️ <b>Buzilsa:</b> uyqusizlik, sutkalik ritm buzilishi. Kechasi telefon ekrani yorug'i melatoninni kamaytirib, uyquni buzadi.
"""),
            ],
        ),
        category(
            "neck",
            "🦋 Qalqonsimon bez",
            "Bo'yindagi bezlar — moddalar almashinuvi va kalsiy boshqaruvchilari.",
            [
                item("thyroid", "Qalqonsimon bez", "Glandula thyroidea", "thyroid",
                     """
<b>Joylashuvi:</b> bo'yinning old qismida, hiqildoq ostida. Kapalak shaklida (2 bo'lak + bo'yincha). Vazni 15–30 g.

<b>Gormonlari:</b>
• <b>Tiroksin (T4) va triyodtironin (T3)</b> — tarkibida <b>yod</b> bor; moddalar almashinuvi tezligi, yurak urishi, tana harorati, bolalarda o'sish va <u>aqliy rivojlanish</u>
• <b>Kalsitonin</b> — qondagi kalsiyni kamaytiradi

⚠️ <b>Buzilsa:</b>
• Gormon <b>ko'p</b> — <i>tireotoksikoz (Bazedov kasalligi)</i>: ozib ketish, ko'z chaqchayishi, yurak tez urishi, qo'l titrashi, asabiylik, terlash
• Gormon <b>kam</b> — <i>gipotireoz</i>: semirish, holsizlik, sovqotish, shishlar, xotira pasayishi
• Bolalikda kam — <i>kretinizm</i>: aqliy va jismoniy orqada qolish
• <b>Yod yetishmasligi</b> — <i>endemik buqoq</i>: bez kattalashadi (O'zbekistonda ham uchraydi — yodlangan tuz ishlatish kerak!)
"""),
                item("parathyroid", "Qalqonsimon bez oldi bezlari", "Glandulae parathyroideae", "parathyroid gland",
                     """
<b>Soni:</b> odatda <b>4 ta</b> (guruch donasidek)
<b>Joylashuvi:</b> qalqonsimon bezning orqa yuzasida

<b>Gormoni:</b> <b>paratgormon</b> — qondagi <b>kalsiyni ko'paytiradi</b> (suyakdan chiqaradi, buyrakda ushlab qoladi, ichakda so'rilishini oshiradi). Kalsitoninga qarama-qarshi.

⚠️ <b>Buzilsa:</b>
• Gormon <b>ko'p</b> — suyaklardan kalsiy chiqib ketadi → suyaklar mo'rtlashadi, sinadi; buyrakda toshlar
• Gormon <b>kam</b> — qonda kalsiy kamayadi → <i>tetaniya</i>: muskullar tortishishi, barmoqlar uvishishi va qotishi
"""),
            ],
        ),
        category(
            "body",
            "⚙️ Tanadagi bezlar",
            "Buyrak usti bezi, oshqozon osti bezi, jinsiy bezlar va ayrisimon bez.",
            [
                item("adrenal", "Buyrak usti bezlari", "Glandulae suprarenales", "adrenal gland",
                     """
<b>Soni:</b> 2 ta, har bir buyrak ustida. Vazni ~5 g.

<b>Po'stloq qavati gormonlari:</b>
• <b>Kortizol</b> — "stress gormoni": qand miqdorini oshiradi, yallig'lanishni bosadi
• <b>Aldosteron</b> — buyrakda natriy va suvni ushlab qoladi → qon bosimini oshiradi
• Jinsiy gormonlar (oz miqdorda)

<b>Mag'iz qavati gormonlari:</b>
• <b>Adrenalin va noradrenalin</b> — "jang yoki qoch": yurak tez uradi, bosim oshadi, qorachiq kengayadi

⚠️ <b>Buzilsa:</b>
• Kortizol <b>ko'p</b> — <i>Itsenko-Kushing sindromi</i>: oy yuz, qorin va bo'yinda yog', qorinda qizil chiziqlar, gipertoniya, diabet
• Kortizol va aldosteron <b>kam</b> — <i>Addison (bronza) kasalligi</i>: teri qorayadi, holsizlik, past bosim, ozish
• Mag'iz o'smasi (feoxromotsitoma) — keskin bosim ko'tarilishlari
"""),
                item("pancreas", "Oshqozon osti bezi (Langergans orolchalari)", "Pancreas, insulae pancreaticae", "pancreas",
                     """
<b>Joylashuvi:</b> oshqozon orqasida, qorin bo'shlig'ida. Uzunligi 15–20 sm.
<b>Aralash bez:</b> hazm shirasi (tashqi sekretsiya) + gormonlar (ichki sekretsiya).

<b>Langergans orolchalari</b> (~1 mln, bez massasining 1–2%):
• <b>β-hujayralar → insulin</b> — qondagi qandni <u>kamaytiradi</u> (glyukozani hujayralarga kiritadi)
• <b>α-hujayralar → glyukagon</b> — qandni <u>oshiradi</u> (jigardan chiqaradi)

<b>Normal qand (och qoringa):</b> 3,3–5,5 mmol/l

⚠️ <b>Buzilsa:</b>
• Insulin <b>kam</b> yoki ta'sir qilmasa — <b>qandli diabet</b> (🩺 Kasalliklar bo'limiga qarang)
• Insulin ko'p (o'sma yoki dozani oshirib yuborish) — <i>gipoglikemiya</i>: titrash, terlash, hushdan ketish
• Bezning yallig'lanishi — <i>pankreatit</i> (ko'pincha spirtli ichimlik va yog'li ovqatdan)
"""),
                item("gonads", "Jinsiy bezlar", "Gonadae (testes, ovaria)", "gonad",
                     """
<b>Erkaklarda — moyaklar:</b>
• <b>Testosteron</b> — erkak jinsiy belgilari: soqol-mo'ylov, past ovoz, muskullar o'sishi, spermatozoidlar hosil bo'lishi

<b>Ayollarda — tuxumdonlar:</b>
• <b>Estrogenlar</b> — ayol jinsiy belgilari, hayz sikli
• <b>Progesteron</b> — "homiladorlik gormoni", bachadonni homilaga tayyorlaydi

Gipofizning FSG va LG gormonlari boshqaradi.

⚠️ <b>Buzilsa:</b> balog'atga yetish kechikishi yoki erta boshlanishi, bepushtlik, hayz sikli buzilishi, tuxumdon polikistozi (ortiqcha androgen — tuk ko'payishi, husnbuzar), menopauzada estrogen kamayishi → osteoporoz.
"""),
                item("thymus", "Ayrisimon bez (timus)", "Thymus", "thymus",
                     """
<b>Joylashuvi:</b> ko'krak qafasining yuqori qismida, to'sh suyagi orqasida.
<b>Xususiyati:</b> bolalikda katta (~35 g), balog'atdan keyin kichrayib, yog'ga aylanadi.

<b>Vazifasi:</b> <b>T-limfotsitlarni</b> "o'rgatadi" — immun tizimining asosi. Timozin gormonini ishlab chiqaradi.

⚠️ <b>Buzilsa:</b> immunitet tanqisligi (tez-tez kasallanish), autoimmun kasalliklar (masalan, <i>miasteniya</i> — muskullar tez charchashi).
"""),
            ],
        ),
        category(
            "dis",
            "🩺 Kasalliklar — qayer buzilsa nima bo'ladi",
            "Gormon ko'p yoki kam bo'lganda kelib chiqadigan asosiy kasalliklar.",
            [
                item("diabetes", "Qandli diabet", "Diabetes mellitus", "diabetes mellitus",
                     """
<b>📍 Qayer buziladi:</b> oshqozon osti bezining β-hujayralari yoki insulinni sezuvchi to'qimalar.

<b>1-tur diabet</b> (~10%):
• Immun tizim β-hujayralarni yemiradi → insulin <b>umuman ishlab chiqarilmaydi</b>
• Ko'pincha bolalik va yoshlikda boshlanadi
• Davolash — umrbod <b>insulin ukoli</b>

<b>2-tur diabet</b> (~90%):
• Insulin bor, lekin hujayralar uni <b>sezmay qoladi</b> (insulinrezistentlik)
• Sabablari: <b>semizlik</b>, kam harakat, ko'p shirinlik, irsiyat; 40 yoshdan keyin ko'p
• Davolash — parhez, harakat, tabletkalar

<b>Belgilari:</b> kuchli chanqoq, ko'p siyish, og'iz qurishi, ozish, teri qichishi, yaralar sekin bitishi.

⚠️ <b>Asoratlari:</b> ko'rlik, buyrak yetishmovchiligi, infarkt, insult, "diabetik oyoq" (amputatsiya).
"""),
                item("goiter", "Endemik buqoq", "Struma endemica", "goitre",
                     """
<b>📍 Qayer buziladi:</b> qalqonsimon bez.

<b>Kelib chiqishi:</b> ovqat va suvda <b>yod yetishmaydi</b> → bez gormon ishlab chiqara olmaydi → gipofiz TTGni ko'paytiradi → bez "zo'riqib" <b>kattalashadi</b>.

<b>Qayerda ko'p:</b> tog'li va dengizdan uzoq hududlarda (O'rta Osiyo ham shu jumladan).

<b>Belgilari:</b> bo'yin old qismi kattalashishi, yutish va nafas olish qiyinlashishi, gipotireoz belgilari.

💡 <b>Oldini olish:</b> yodlangan tuz, dengiz mahsulotlari, yong'oq.
"""),
                item("graves", "Tireotoksikoz (Bazedov kasalligi)", "Morbus Basedow", "graves disease",
                     """
<b>📍 Qayer buziladi:</b> qalqonsimon bez <b>ortiqcha</b> gormon ishlab chiqaradi.

<b>Kelib chiqishi:</b> autoimmun kasallik — immun tizim antitanachalari bezni doimiy qo'zg'atadi. Stress, irsiyat, ayollarda ko'proq.

<b>Belgilari:</b>
• Ko'p ovqat yeyishiga qaramay ozish
• Yurak tez urishi (100+), qo'l titrashi
• <b>Ko'zlar chaqchayishi</b> (ekzoftalm)
• Asabiylik, terlash, issiqni ko'tara olmaslik
• Bo'yinda bez kattalashishi
"""),
                item("hypothyroid", "Gipotireoz", "Hypothyreosis", "hypothyroidism",
                     """
<b>📍 Qayer buziladi:</b> qalqonsimon bez <b>kam</b> gormon ishlab chiqaradi.

<b>Kelib chiqish sabablari:</b> autoimmun tireoidit (Xashimoto), yod yetishmasligi, bez operatsiyasidan keyin, gipofiz kasalligi.

<b>Belgilari:</b> semirish, sekinlik, uyquchanlik, sovqotish, quruq teri, soch to'kilishi, yuz va qo'llar shishishi, ich qotishi, xotira pasayishi.

⚠️ Bolalikda davolanmasa — <i>kretinizm</i>. Shuning uchun chaqaloqlar tug'ruqxonada tekshiriladi.
"""),
                item("growthdis", "Gigantizm, akromegaliya va pakanalik", "Gigantismus, acromegalia, nanismus", "acromegaly",
                     """
<b>📍 Qayer buziladi:</b> gipofiz — o'sish gormoni (STG).

📈 <b>STG ko'p:</b>
• Bolalikda (o'sish zonalari ochiq) — <b>gigantizm</b>: bo'y 2 m dan oshadi
• Kattalarda — <b>akromegaliya</b>: bo'y o'smaydi, lekin qo'l-oyoq panjalari, burun, quloq, pastki jag', til kattalashadi
• Sababi — ko'pincha gipofiz o'smasi (adenoma)

📉 <b>STG kam (bolalikda):</b>
• <b>Gipofizar pakanalik</b> — bo'y 130 sm dan past, tana nisbati to'g'ri, aql normal
• Davolash — bolalikda o'sish gormoni ukollari
"""),
                item("cushing", "Itsenko-Kushing va Addison kasalliklari", "Morbus Cushing, morbus Addison", "cushing syndrome",
                     """
<b>📍 Qayer buziladi:</b> buyrak usti bezi po'stlog'i (yoki uni boshqaruvchi gipofiz).

📈 <b>Kortizol KO'P — Itsenko-Kushing:</b>
• Sabab: gipofiz yoki buyrak usti bezi o'smasi, gormonal dorilarni uzoq ichish
• Belgilar: oy shaklidagi qizil yuz, qorin va bo'yin orqasida yog' (qo'l-oyoqlar ingichka), qorinda binafsha chiziqlar, gipertoniya, suyak mo'rtligi, diabet

📉 <b>Kortizol KAM — Addison (bronza kasalligi):</b>
• Sabab: autoimmun yemirilish, sil
• Belgilar: teri va shilliq qavatlar qorayishi (bronza tus), holsizlik, ozish, past qon bosimi, tuzli ovqatga ishtiyoq
"""),
            ],
        ),
    ],
)
