from .common import category, item, section

BLOOD = section(
    "qon",
    "❤️ Qon aylanish tizimi",
    """
<b>❤️ QON AYLANISH TIZIMI</b>

<b>Tarkibi:</b> yurak, qon tomirlari (arteriyalar, venalar, kapillyarlar) va qon.

<b>Raqamlar:</b>
• Yurak sutkasiga <b>~100 000</b> marta uradi va <b>~7 000 litr</b> qon haydaydi
• Kattalarda qon hajmi — <b>4,5–5,5 litr</b> (tana vaznining ~7–8%)
• Barcha qon tomirlari uzunligi — <b>~100 000 km</b> (Yer aylanasidan 2,5 marta uzun!)
• Qon butun tanani <b>~1 daqiqada</b> aylanib chiqadi

<b>Ikki doira:</b>
• <b>Katta doira</b> — chap qorincha → aorta → butun tana → kovak venalar → o'ng bo'lmacha
• <b>Kichik (o'pka) doira</b> — o'ng qorincha → o'pka arteriyasi → o'pka (kislorod oladi) → o'pka venalari → chap bo'lmacha

Mavzuni tanlang 👇
""",
    [
        category(
            "heart",
            "❤️ Yurak",
            "Yurak — qonni haydovchi muskulli nasos.",
            [
                item("heart", "Yurak tuzilishi", "Cor", "heart",
                     """
<b>Joylashuvi:</b> ko'krak qafasida, ikki o'pka orasida, 2/3 qismi chap tomonda
<b>O'lchami:</b> mushtdek, vazni 250–350 g

<b>4 ta kamera:</b>
• <b>O'ng bo'lmacha</b> — tanadan venoz qonni qabul qiladi
• <b>O'ng qorincha</b> — qonni o'pkaga haydaydi
• <b>Chap bo'lmacha</b> — o'pkadan kislorodli qonni qabul qiladi
• <b>Chap qorincha</b> — qonni butun tanaga haydaydi (devori eng qalin — 10–15 mm)

<b>Devor qavatlari:</b> endokard (ichki), <b>miokard</b> (muskul), epikard (tashqi) + perikard xaltasi.

⚠️ <b>Buzilsa:</b> yurak ishemik kasalligi, infarkt, yurak yetishmovchiligi, aritmiya, yurak nuqsonlari.
"""),
                item("valves", "Yurak klapanlari", "Valvae cordis", "heart valves",
                     """
<b>4 ta klapan</b> qonni faqat bir tomonga o'tkazadi:
• <b>Uch tavaqali</b> — o'ng bo'lmacha va qorincha orasida
• <b>Ikki tavaqali (mitral)</b> — chap bo'lmacha va qorincha orasida
• <b>O'pka arteriyasi klapani</b> — o'ng qorincha chiqishida
• <b>Aorta klapani</b> — chap qorincha chiqishida

💡 Yurak urishi tovushi "tuk-tak" — klapanlarning yopilish ovozi.

⚠️ <b>Buzilsa:</b> <i>yurak nuqsoni</i> — klapan torayishi (stenoz) yoki to'liq yopilmasligi (yetishmovchilik). Ko'pincha <b>revmatizm</b> (davolanmagan angina asorati) yoki tug'ma sabab bo'ladi. Natija — hansirash, shishlar, yurak yetishmovchiligi.
"""),
                item("conduction", "Yurak o'tkazuvchi tizimi", "Systema conducens cordis", "cardiac conduction system",
                     """
<b>Yurak o'zini o'zi qo'zg'atadi</b> — maxsus hujayralar elektr impuls hosil qiladi:
1. <b>Sinus tuguni</b> — "yurak ritmi boshlovchisi", daqiqasiga 60–80 impuls
2. <b>Bo'lmacha-qorincha tuguni</b> — impulsni biroz ushlab turadi
3. <b>Gis tutami</b> va oyoqchalari
4. <b>Purkine tolalari</b> — qorinchalar muskuliga tarqatadi

<b>Normal puls:</b> daqiqasiga 60–90 marta.
EKG — aynan shu elektr faollikni yozib oladi.

⚠️ <b>Buzilsa:</b> <i>aritmiya</i> — yurak notekis, juda tez (taxikardiya) yoki sekin (bradikardiya) uradi; blokadalarda yurakka sun'iy ritm boshlovchi (kardiostimulyator) qo'yiladi.
"""),
                item("coronary", "Yurak toj arteriyalari", "Arteriae coronariae", "coronary arteries",
                     """
<b>Vazifasi:</b> yurak muskulining <b>o'zini</b> qon bilan ta'minlash.
<b>Boshlanishi:</b> aortaning eng boshidan — o'ng va chap toj arteriyalar.

⚠️ <b>Buzilsa:</b> toj arteriyalarida <b>ateroskleroz</b> (xolesterin blyashkalari) → tomir torayadi → <i>stenokardiya</i> (yurak sohasida siquvchi og'riq). Tomir butunlay tiqilsa → <b>miokard infarkti</b>.
"""),
            ],
        ),
        category(
            "vessels",
            "🩸 Qon tomirlari va qon",
            "Arteriyalar, venalar, kapillyarlar va qon tarkibi.",
            [
                item("aorta", "Aorta va arteriyalar", "Aorta, arteriae", "aorta",
                     """
<b>Arteriyalar</b> — qonni <u>yurakdan</u> olib ketadi. Devori qalin, elastik, muskulli (yuqori bosimga chidaydi).

<b>Aorta</b> — eng katta arteriya (diametri ~2,5–3 sm). Chap qorinchadan chiqib, ravoq hosil qiladi va pastga tushadi.
<b>Asosiy shoxlari:</b>
• Uyqu arteriyalari — bosh miya va yuzga
• O'mrov osti arteriyalari — qo'llarga
• Qorin aortasi shoxlari — ichki a'zolar, buyraklar
• Yonbosh arteriyalari — chanoq va oyoqlarga

💡 Puls — arteriya devorining tebranishi (bilakda, bo'yinda seziladi).

⚠️ <b>Buzilsa:</b> ateroskleroz, aorta anevrizmasi (devorning bo'rtib chiqishi — yorilsa o'ta xavfli), gipertoniya.
"""),
                item("veins", "Venalar", "Venae", "vein",
                     """
<b>Venalar</b> — qonni <u>yurakka</u> qaytaradi. Devori yupqa, bosimi past.

<b>Xususiyati:</b> oyoq va qo'l venalarida <b>klapanlar</b> bor — qonning pastga qaytib oqishiga yo'l qo'ymaydi. Muskullar qisqarib venalarni siqadi va qonni yuqoriga haydaydi.

<b>Eng katta venalar:</b> yuqori va pastki kovak venalar — o'ng bo'lmachaga quyiladi.
<b>Darvoza venasi</b> — ichakdan qonni jigarga olib boradi.

⚠️ <b>Buzilsa:</b>
• <i>Varikoz</i> — klapanlar ishlamay qoladi, oyoq venalari kengayib bo'rtadi (uzoq tik turish, irsiyat)
• <i>Tromboz</i> — venada qon laxtasi; uzilib o'pkaga borsa — o'pka arteriyasi tromboemboliyasi (o'limga olib kelishi mumkin)
"""),
                item("capillary", "Kapillyarlar", "Vasa capillaria", "capillary",
                     """
<b>Kapillyarlar</b> — eng mayda qon tomirlari, arteriya va venalarni bog'laydi.
• Diametri <b>5–10 mkm</b> — eritrotsitlar bittalab o'tadi
• Devori bitta qavat hujayradan iborat

<b>Vazifasi:</b> qon va to'qimalar orasida <b>moddalar almashinuvi</b> — kislorod va oziq beriladi, CO₂ va chiqindilar olinadi.

⚠️ <b>Buzilsa:</b> qandli diabetda kapillyarlar zararlanadi — ko'z (retinopatiya, ko'rlik), buyrak (nefropatiya), oyoq (yaralar, "diabetik oyoq").
"""),
                item("blood", "Qon tarkibi", "Sanguis", "blood cells",
                     """
<b>Qon</b> = <b>plazma</b> (~55%) + <b>shaklli elementlar</b> (~45%)

🔴 <b>Eritrotsitlar</b> — 4–5,5 mln/mkl; gemoglobin orqali kislorod tashiydi. Yashash muddati ~120 kun.
⚪️ <b>Leykotsitlar</b> — 4–9 ming/mkl; organizmni mikroblardan himoya qiladi (immunitet).
🟣 <b>Trombotsitlar</b> — 180–320 ming/mkl; qon ivishini ta'minlaydi.

<b>Plazma:</b> 90% suv + oqsillar, tuzlar, glyukoza, gormonlar.
<b>Hosil bo'lishi:</b> qizil suyak ko'migida.

⚠️ <b>Buzilsa:</b>
• Eritrotsit/gemoglobin kam — <i>kamqonlik (anemiya)</i>
• Leykotsitlar nazoratsiz ko'paysa — <i>leykoz</i> (qon raki)
• Trombotsit kam yoki ivish omili yo'q — qon ketishi, <i>gemofiliya</i>
"""),
            ],
        ),
        category(
            "dis",
            "🩺 Kasalliklar — qayer buzilsa nima bo'ladi",
            "Qon aylanish tizimining qaysi qismi buzilganda qanday kasallik kelib chiqadi.",
            [
                item("hypertension", "Gipertoniya (yuqori qon bosimi)", "Hypertensio arterialis", "hypertension",
                     """
<b>📍 Qayer buziladi:</b> arteriyalar tonusi va bosimni boshqaruvchi tizimlar (buyrak, gormonlar, nerv tizimi).
<b>Norma:</b> ~120/80 mm sim. ust. <b>Gipertoniya:</b> 140/90 va undan yuqori.

<b>Kelib chiqish sabablari:</b>
• Ko'p tuz iste'mol qilish, ortiqcha vazn, kam harakat
• Stress, chekish, spirtli ichimliklar
• Irsiyat, yosh
• Buyrak kasalliklari, gormon buzilishlari (ikkilamchi gipertoniya)

<b>Belgilari:</b> ko'pincha <b>sezilmaydi</b> ("jim qotil"); bosh og'rig'i (ensada), bosh aylanishi, quloq shang'illashi.

⚠️ <b>Asoratlari:</b> insult, infarkt, buyrak yetishmovchiligi, ko'z to'r pardasi zararlanishi.
"""),
                item("athero", "Ateroskleroz", "Atherosclerosis", "atherosclerosis",
                     """
<b>📍 Qayer buziladi:</b> arteriyalarning ichki devori.

<b>Kelib chiqishi:</b> tomir devorida <b>xolesterin blyashkalari</b> to'planadi → tomir torayadi va qattiqlashadi → qon oqimi kamayadi. Blyashka yorilsa, ustida qon laxtasi hosil bo'lib tomirni butunlay tiqib qo'yadi.

<b>Xavf omillari:</b> yog'li ovqat, yuqori xolesterin, chekish, diabet, gipertoniya, semizlik, kam harakat.

<b>Qayerda bo'lsa — qanday kasallik:</b>
• Yurak tomirlarida → stenokardiya, <b>infarkt</b>
• Miya tomirlarida → <b>insult</b>
• Oyoq tomirlarida → oqsoqlanish, gangrena
• Buyrak tomirlarida → gipertoniya
"""),
                item("infarct", "Miokard infarkti", "Infarctus myocardii", "myocardial infarction",
                     """
<b>📍 Qayer buziladi:</b> yurak toj arteriyasi tiqiladi → yurak muskulining bir qismi qonsiz qolib <b>nobud bo'ladi</b>.

<b>Kelib chiqish sababi:</b> ateroskleroz blyashkasi yorilib, ustida tromb hosil bo'lishi.

<b>Belgilari:</b>
• Ko'krak ortida <b>kuchli siquvchi, kuyduruvchi og'riq</b> (20 daqiqadan ko'p)
• Og'riq chap qo'lga, jag'ga, kurak orasiga tarqaladi
• Sovuq ter, qo'rquv, hansirash

🚑 <b>Darhol 103 ga qo'ng'iroq qiling!</b> Birinchi soatlarda davolash yurak muskulini saqlab qoladi.
"""),
                item("stroke", "Insult", "Insultus cerebri", "stroke",
                     """
<b>📍 Qayer buziladi:</b> bosh miya qon tomirlari.

<b>2 turi:</b>
• <b>Ishemik</b> (~85%) — miya arteriyasi tromb bilan tiqiladi (ateroskleroz, aritmiyada yurakdan kelgan tromb)
• <b>Gemorragik</b> — miya tomiri yoriladi, miyaga qon quyiladi (ko'pincha yuqori bosimda)

<b>Belgilari ("YUZ-QO'L-NUTQ" testi):</b>
• Yuzning bir tomoni osilib qoladi
• Bir tomondagi qo'l-oyoq kuchsizlanadi
• Nutq buziladi, tushunmaydi

🚑 Darhol 103! Birinchi 4,5 soat — "oltin vaqt".
"""),
                item("anemia", "Kamqonlik (anemiya)", "Anaemia", "anemia",
                     """
<b>📍 Qayer buziladi:</b> qondagi eritrotsitlar va gemoglobin miqdori kamayadi → to'qimalarga kam kislorod boradi.

<b>Kelib chiqish sabablari:</b>
• <b>Temir yetishmasligi</b> — eng ko'p sabab (kam go'sht, ko'p qon yo'qotish, homiladorlik)
• B12 vitamini va foliy kislotasi yetishmasligi
• Suyak ko'migi kasalliklari
• Eritrotsitlarning ko'p parchalanishi (gemolitik anemiya)
• Buyrak yetishmovchiligi (eritropoetin kamayadi)

<b>Belgilari:</b> rangparlik, holsizlik, bosh aylanishi, hansirash, sochlar to'kilishi, tirnoqlar mo'rtlashishi.
"""),
                item("heartfail", "Yurak yetishmovchiligi", "Insufficientia cordis", "heart failure",
                     """
<b>📍 Qayer buziladi:</b> yurak muskuli (miokard) qonni yetarli haydab bera olmaydi.

<b>Kelib chiqish sabablari:</b> infarktdan keyingi chandiq, uzoq yillik gipertoniya, yurak nuqsonlari, kardiomiopatiya, aritmiya.

<b>Belgilari:</b>
• Chap qorincha — qon o'pkada turib qoladi → <b>hansirash</b>, yotganda bo'g'ilish
• O'ng qorincha — qon tanada turib qoladi → <b>oyoq shishlari</b>, jigar kattalashishi
• Tez charchash
"""),
            ],
        ),
    ],
)
