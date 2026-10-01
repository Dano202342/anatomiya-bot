from .common import category, item, section

MUSCLES = section(
    "musk",
    "💪 Muskullar",
    """
<b>💪 MUSKUL TIZIMI</b>

Odam tanasida <b>600 dan ortiq</b> skelet muskuli bor. Ular tana vaznining <b>~40%</b> ini tashkil etadi.

<b>Muskul to'qimasining 3 turi:</b>
• <b>Skelet (ko'ndalang-targ'il)</b> — ixtiyoriy, suyaklarni harakatlantiradi
• <b>Silliq</b> — ixtiyorsiz, ichki a'zolar va qon tomirlar devorida
• <b>Yurak muskuli</b> — ixtiyorsiz, faqat yurakda, charchamaydi

<b>Skelet muskuli tuzilishi:</b> muskul → tutamlar → muskul tolalari → miofibrillalar → aktin va miozin
Har bir muskulning <b>boshlanishi</b> (qo'zg'almas nuqta) va <b>birikishi</b> (harakatlanuvchi nuqta) bor.

💡 Eng katta muskul — katta dumba muskuli; eng kichigi — uzangi muskuli (1 mm).
Muskul guruhini tanlang 👇
""",
    [
        category(
            "head",
            "😊 Bosh muskullari",
            "Bosh muskullari 2 guruh: <b>mimika muskullari</b> (yuz ifodasi) va <b>chaynov muskullari</b>.",
            [
                item("frontalis", "Peshona-ensa muskuli", "M. occipitofrontalis", "occipitofrontalis muscle",
                     """
<b>Joylashuvi:</b> kalla gumbazi; peshona va ensa qorinchalaridan iborat, o'rtada pay dubulg'asi
<b>Boshlanishi:</b> ensa suyagi / pay dubulg'asi
<b>Birikishi:</b> qosh terisi

<b>Vazifasi:</b> qoshlarni ko'tarish, peshonada ko'ndalang ajinlar hosil qilish (hayratlanish ifodasi)
<b>Nervi:</b> yuz nervi (VII)
""", q="occipitofrontalis"),
                item("orboculi", "Ko'zning aylana muskuli", "M. orbicularis oculi", "orbicularis oculi",
                     """
<b>Joylashuvi:</b> ko'z kosasi atrofida, qovoqlarda aylana shaklda
<b>Vazifasi:</b> ko'zni yumish, ko'z qisish, ko'z yoshini oqizishga yordam
<b>Nervi:</b> yuz nervi (VII)

💡 Odam kuniga ~15 000–20 000 marta ko'z qisadi — bu muskul eng faol muskullardan biri.
"""),
                item("ororis", "Og'izning aylana muskuli", "M. orbicularis oris", "orbicularis oris",
                     """
<b>Joylashuvi:</b> lablar qalinligida, og'iz tirqishi atrofida
<b>Vazifasi:</b> og'izni yumish, lablarni cho'chchaytirish (o'pish, hushtak chalish), nutq
<b>Nervi:</b> yuz nervi (VII)
"""),
                item("zygomatic", "Katta yonoq muskuli", "M. zygomaticus major", "zygomaticus major",
                     """
<b>Boshlanishi:</b> yonoq suyagi
<b>Birikishi:</b> og'iz burchagi
<b>Vazifasi:</b> og'iz burchagini yuqoriga-tashqariga tortish — <b>tabassum muskuli</b> 😊
<b>Nervi:</b> yuz nervi (VII)
"""),
                item("buccinator", "Lunj muskuli", "M. buccinator", "buccinator",
                     """
<b>Joylashuvi:</b> lunj devorining asosi
<b>Boshlanishi:</b> yuqori va pastki jag'ning alveolyar o'simtalari
<b>Vazifasi:</b> lunjni tishlarga bosish (ovqatni tishlar orasida ushlash), puflash, karnay chalish
<b>Nervi:</b> yuz nervi (VII)
"""),
                item("masseter", "Chaynov muskuli", "M. masseter", "masseter muscle",
                     """
<b>Boshlanishi:</b> yonoq ravog'i
<b>Birikishi:</b> pastki jag' burchagining tashqi yuzasi
<b>Vazifasi:</b> pastki jag'ni ko'tarish — tishlarni qisish
<b>Nervi:</b> uch shoxli nerv (V3)

💡 O'z o'lchamiga nisbatan <b>eng kuchli muskul</b> — oziq tishlarda ~70–90 kg bosim hosil qiladi!
"""),
                item("temporalis", "Chakka muskuli", "M. temporalis", "temporalis muscle",
                     """
<b>Boshlanishi:</b> chakka chuqurchasi (yelpig'ich shaklida)
<b>Birikishi:</b> pastki jag'ning tojsimon o'simtasi
<b>Vazifasi:</b> pastki jag'ni ko'tarish va orqaga tortish
<b>Nervi:</b> uch shoxli nerv (V3)

💡 Chaynayotganda chakkangizga qo'lingizni qo'ysangiz, uning qisqarishini sezasiz.
"""),
                item("pterygoid", "Qanotsimon muskullar", "Mm. pterygoidei medialis et lateralis", "pterygoid muscles",
                     """
<b>Joylashuvi:</b> pastki jag' ichki tomonida, ponasimon suyakning qanotsimon o'simtasidan boshlanadi

• <b>Medial qanotsimon</b> — jag'ni ko'taradi (chaynov muskuliga sherik)
• <b>Lateral qanotsimon</b> — og'izni ochadi, jag'ni oldinga va yon tomonga suradi (maydalash harakati)

<b>Nervi:</b> uch shoxli nerv (V3)
""", q="lateral pterygoid"),
            ],
        ),
        category(
            "neck",
            "🦒 Bo'yin muskullari",
            "Bo'yin muskullari boshni harakatlantiradi, yutish va nafas olishda qatnashadi.",
            [
                item("platysma", "Bo'yin teri osti muskuli", "Platysma", "platysma",
                     """
<b>Joylashuvi:</b> bo'yinning old yuzasida, bevosita teri ostida (yupqa varaq)
<b>Boshlanishi:</b> ko'krakning yuqori qismi fassiyasi
<b>Birikishi:</b> pastki jag' va og'iz burchagi
<b>Vazifasi:</b> bo'yin terisini tortish, og'iz burchagini pastga tushirish (qo'rquv ifodasi)
<b>Nervi:</b> yuz nervi (VII)
"""),
                item("scm", "To'sh-o'mrov-so'rg'ichsimon muskul", "M. sternocleidomastoideus", "sternocleidomastoid muscle",
                     """
<b>Boshlanishi:</b> 2 boshcha — to'sh suyagi dastasi va o'mrov suyagi
<b>Birikishi:</b> chakka suyagining so'rg'ichsimon o'simtasi
<b>Vazifasi:</b>
• Bir tomonlama — boshni qarama-qarshi tomonga burish, o'z tomoniga egish
• Ikki tomonlama — boshni orqaga tashlash; nafas olishga yordam
<b>Nervi:</b> qo'shimcha nerv (XI)

💡 Bo'yinning eng ko'zga ko'rinadigan muskuli; bo'yinni old va yon uchburchaklarga bo'ladi.
"""),
                item("scalene", "Narvonsimon muskullar", "Mm. scaleni", "scalene muscles",
                     """
<b>Soni:</b> 3 juft — oldingi, o'rta, orqa
<b>Boshlanishi:</b> bo'yin umurtqalarining ko'ndalang o'simtalari
<b>Birikishi:</b> I va II qovurg'alar
<b>Vazifasi:</b> qovurg'alarni ko'tarish (chuqur nafas olish), bo'yinni yon tomonga egish

💡 Oldingi va o'rta narvonsimon muskullar orasidan <b>yelka chigali</b> va o'mrov osti arteriyasi o'tadi.
""", q="anterior scalene"),
                item("hyoid", "Til osti suyagi muskullari", "Mm. suprahyoidei et infrahyoidei", "suprahyoid muscles",
                     """
<b>Til osti suyagidan yuqoridagilar (4 juft):</b> ikki qorinchali, bigizsimon-til osti, jag'-til osti, iyak-til osti — og'iz tubini hosil qiladi, og'izni ochadi, yutishda til osti suyagini ko'taradi.

<b>Til osti suyagidan pastdagilar (4 juft):</b> to'sh-til osti, to'sh-qalqonsimon, qalqonsimon-til osti, kurak-til osti — til osti suyagi va hiqildoqni pastga tushiradi.

<b>Vazifasi:</b> yutish, gapirish.
""", q="digastric muscle"),
            ],
        ),
        category(
            "chest",
            "🫁 Ko'krak muskullari",
            "Ko'krak muskullari qo'lni harakatlantiradi va nafas olishda qatnashadi.",
            [
                item("pecmaj", "Katta ko'krak muskuli", "M. pectoralis major", "pectoralis major",
                     """
<b>Boshlanishi:</b> o'mrov suyagi, to'sh suyagi, yuqori 6 qovurg'a tog'aylari, qorin to'g'ri muskuli qini
<b>Birikishi:</b> yelka suyagining katta do'mbog'i qirrasi
<b>Vazifasi:</b> qo'lni tanaga yaqinlashtirish, ichkariga burish, oldinga ko'tarish (quchoqlash, itarish)
<b>Nervi:</b> medial va lateral ko'krak nervlari (C5–T1)

🏋️ Mashq: shtanga ko'tarish, otjimaniya.
"""),
                item("pecmin", "Kichik ko'krak muskuli", "M. pectoralis minor", "pectoralis minor",
                     """
<b>Joylashuvi:</b> katta ko'krak muskuli ostida
<b>Boshlanishi:</b> III–V qovurg'alar
<b>Birikishi:</b> kurakning tumshuqsimon o'simtasi
<b>Vazifasi:</b> kurakni oldinga-pastga tortish; kurak qo'zg'almas bo'lsa qovurg'alarni ko'taradi (nafasga yordam)
"""),
                item("serratus", "Oldingi tishli muskul", "M. serratus anterior", "serratus anterior",
                     """
<b>Boshlanishi:</b> yuqori 8–9 qovurg'a (arra tishlari ko'rinishida)
<b>Birikishi:</b> kurakning ichki qirrasi
<b>Vazifasi:</b> kurakni ko'krak qafasiga bosib turish va oldinga surish (musht tushirish) — "bokschi muskuli"
<b>Nervi:</b> uzun ko'krak nervi

⚠️ Falajlanganda — <i>"qanotsimon kurak"</i>.
"""),
                item("intercostm", "Qovurg'alararo muskullar", "Mm. intercostales", "intercostal muscles",
                     """
<b>Joylashuvi:</b> qovurg'alar orasidagi bo'shliqlarda, 11 juft oraliqda
• <b>Tashqi</b> — qovurg'alarni ko'taradi → <b>nafas olish</b>
• <b>Ichki</b> — qovurg'alarni tushiradi → <b>nafas chiqarish</b>
<b>Nervi:</b> qovurg'alararo nervlar
"""),
                item("diaphragm", "Diafragma", "Diaphragma", "thoracic diaphragm",
                     """
<b>Joylashuvi:</b> ko'krak va qorin bo'shliqlari orasidagi gumbazsimon to'siq
<b>Boshlanishi:</b> to'sh suyagi, pastki 6 qovurg'a, bel umurtqalari
<b>Birikishi:</b> markazdagi pay markazi

<b>Vazifasi:</b> <b>asosiy nafas muskuli</b> — qisqarganda pastga tushib, o'pkaga havo kiradi (nafas olishning ~70%)
<b>Nervi:</b> diafragma nervi (C3–C5)

<b>Teshiklari:</b> pastki kovak vena, qizilo'ngach, aorta o'tadi.
""", q="diaphragm"),
            ],
        ),
        category(
            "abdomen",
            "🔲 Qorin muskullari",
            "Qorin devori muskullari ichki a'zolarni himoya qiladi, tanani egadi va \"qorin pressi\"ni hosil qiladi.",
            [
                item("rectusabd", "Qorinning to'g'ri muskuli", "M. rectus abdominis", "rectus abdominis",
                     """
<b>Boshlanishi:</b> qov suyagi
<b>Birikishi:</b> V–VII qovurg'a tog'aylari, xanjarsimon o'simta
<b>Vazifasi:</b> tanani oldinga egish, qorin pressi (yo'tal, tug'ish, defekatsiya)
<b>Nervi:</b> T7–T12 qovurg'alararo nervlar

💡 Pay to'siqlari uni 3–4 bo'lakka bo'ladi — mashhur <b>"kubiklar"</b> (six-pack) aynan shu.
"""),
                item("extobl", "Qorinning tashqi qiyshiq muskuli", "M. obliquus externus abdominis", "external oblique muscle",
                     """
<b>Joylashuvi:</b> qorin yon devorining eng yuza qavati
<b>Boshlanishi:</b> pastki 8 qovurg'a
<b>Birikishi:</b> yonbosh suyagi qirrasi, oq chiziq; pastki qirrasi <b>chov boylamini</b> hosil qiladi
<b>Vazifasi:</b> tanani qarama-qarshi tomonga burish, yonga egish
<b>Tola yo'nalishi:</b> "qo'lni cho'ntakka solgandek" — yuqoridan pastga-ichkariga
""", q="external oblique"),
                item("intobl", "Qorinning ichki qiyshiq muskuli", "M. obliquus internus abdominis", "internal oblique muscle",
                     """
<b>Joylashuvi:</b> tashqi qiyshiq muskul ostida (o'rta qavat)
<b>Boshlanishi:</b> bel-ko'krak fassiyasi, yonbosh suyagi qirrasi, chov boylami
<b>Birikishi:</b> pastki 3–4 qovurg'a, oq chiziq
<b>Vazifasi:</b> tanani o'z tomoniga burish, egish; qorin pressi
<b>Tola yo'nalishi:</b> tashqi qiyshiqqa perpendikulyar
""", q="internal oblique"),
                item("transvabd", "Qorinning ko'ndalang muskuli", "M. transversus abdominis", "transversus abdominis",
                     """
<b>Joylashuvi:</b> qorin devorining eng chuqur qavati
<b>Tola yo'nalishi:</b> gorizontal ("korset" kabi)
<b>Vazifasi:</b> qorin bo'shlig'ini siqish, umurtqa pog'onasini barqarorlashtirish, chuqur nafas chiqarish

💡 Tabiiy "kamar" — bel og'rig'ining oldini olishda muhim.
"""),
            ],
        ),
        category(
            "back",
            "🔙 Orqa muskullari",
            "Orqa muskullari yuza (qo'l va kurakni harakatlantiradi) va chuqur (umurtqa pog'onasini tutib turadi) guruhlarga bo'linadi.",
            [
                item("trapezius", "Trapetsiyasimon muskul", "M. trapezius", "trapezius",
                     """
<b>Boshlanishi:</b> ensa suyagi, barcha bo'yin va ko'krak umurtqalarining o'tkir o'simtalari
<b>Birikishi:</b> o'mrov suyagi, kurak qirrasi va yelka o'simtasi
<b>Vazifasi:</b>
• Yuqori tolalari — yelkani ko'tarish ("yelka qisish")
• O'rta — kuraklarni yaqinlashtirish
• Pastki — kurakni pastga tushirish
<b>Nervi:</b> qo'shimcha nerv (XI)

💡 Ikkala tomon birgalikda trapetsiya (romb) shaklini hosil qiladi.
"""),
                item("latissimus", "Orqaning eng keng muskuli", "M. latissimus dorsi", "latissimus dorsi",
                     """
<b>Boshlanishi:</b> pastki 6 ko'krak va barcha bel umurtqalari, dumg'aza, yonbosh suyagi qirrasi
<b>Birikishi:</b> yelka suyagining kichik do'mbog'i qirrasi
<b>Vazifasi:</b> qo'lni pastga tushirish, orqaga tortish, ichkariga burish (turnikda tortilish, eshkak eshish, suzish)
<b>Nervi:</b> ko'krak-orqa nervi (C6–C8)

💡 Tanadagi <b>eng keng</b> muskul — "V" shaklidagi qomat beradi.
"""),
                item("rhomboid", "Rombsimon muskullar", "Mm. rhomboidei major et minor", "rhomboid muscles",
                     """
<b>Joylashuvi:</b> trapetsiyasimon muskul ostida, kuraklar orasida
<b>Boshlanishi:</b> C7–T5 umurtqalarining o'tkir o'simtalari
<b>Birikishi:</b> kurakning ichki qirrasi
<b>Vazifasi:</b> kuraklarni umurtqa pog'onasiga yaqinlashtirish (qomatni to'g'ri tutish)
""", q="rhomboid major"),
                item("levscap", "Kurakni ko'taruvchi muskul", "M. levator scapulae", "levator scapulae",
                     """
<b>Boshlanishi:</b> C1–C4 umurtqalarining ko'ndalang o'simtalari
<b>Birikishi:</b> kurakning yuqori burchagi
<b>Vazifasi:</b> kurakni ko'tarish, bo'yinni egish

💡 Stress va uzoq kompyuterda o'tirganda ko'pincha tarang bo'lib og'riydi.
"""),
                item("erector", "Umurtqa pog'onasini to'g'rilovchi muskul", "M. erector spinae", "erector spinae",
                     """
<b>Joylashuvi:</b> umurtqa pog'onasining ikki tomonida, dumg'azadan ensagacha
<b>3 qismi:</b> yonbosh-qovurg'a, eng uzun, o'tkir o'simta muskullari
<b>Vazifasi:</b> tanani tik tutish, orqaga egilish, umurtqa pog'onasini yozish

💡 Tanadagi eng uzun muskul guruhi — qomatning asosiy tayanchi.
"""),
            ],
        ),
        category(
            "arm",
            "💪 Yelka va qo'l muskullari",
            "Yelka kamari va yelka (qo'lning yuqori qismi) muskullari.",
            [
                item("deltoid", "Deltasimon muskul", "M. deltoideus", "deltoid muscle",
                     """
<b>Boshlanishi:</b> o'mrov suyagi, kurakning yelka o'simtasi va qirrasi
<b>Birikishi:</b> yelka suyagidagi deltasimon g'adir-budur joy
<b>Vazifasi:</b>
• Old qismi — qo'lni oldinga ko'tarish
• O'rta qismi — qo'lni yon tomonga ko'tarish (90° gacha)
• Orqa qismi — qo'lni orqaga tortish
<b>Nervi:</b> qo'ltiq nervi

💡 Shakli yunoncha "Δ" (delta) harfiga o'xshaydi. Ukol qilinadigan joylardan biri.
"""),
                item("rotcuff", "Rotator manjeta muskullari", "Mm. supraspinatus, infraspinatus, teres minor, subscapularis", "rotator cuff",
                     """
<b>4 ta muskul</b> (yelka bo'g'imini "manjeta" kabi o'rab turadi):
• <b>Qirra usti muskuli</b> — qo'lni yonga ko'tarishni boshlaydi
• <b>Qirra osti muskuli</b> — qo'lni tashqariga buradi
• <b>Kichik yumaloq muskul</b> — qo'lni tashqariga buradi
• <b>Kurak osti muskuli</b> — qo'lni ichkariga buradi

<b>Vazifasi:</b> yelka suyagi boshchasini bo'g'im chuqurchasida mahkam ushlab turish.
⚠️ Sportchilarda yirtilishi ko'p uchraydi.
"""),
                item("biceps", "Yelkaning ikki boshli muskuli", "M. biceps brachii", "biceps brachii",
                     """
<b>Boshlanishi:</b> 2 boshcha —
• Uzun boshcha: kurakning bo'g'im usti do'mbog'i
• Kalta boshcha: kurakning tumshuqsimon o'simtasi
<b>Birikishi:</b> bilak (radius) suyagi do'mbog'i
<b>Vazifasi:</b> tirsakni bukish, bilakni tashqariga burish (vintni burash)
<b>Nervi:</b> mushak-teri nervi

🏋️ Mashq: gantel bilan qo'lni bukish.
"""),
                item("brachialis", "Yelka muskuli", "M. brachialis", "brachialis muscle",
                     """
<b>Joylashuvi:</b> ikki boshli muskul ostida
<b>Boshlanishi:</b> yelka suyagining pastki yarmi old yuzasi
<b>Birikishi:</b> tirsak suyagi do'mbog'i
<b>Vazifasi:</b> tirsakni bukuvchi <b>asosiy</b> muskul (bilak qanday holatda bo'lmasin)
<b>Nervi:</b> mushak-teri nervi
"""),
                item("coracobr", "Tumshuqsimon-yelka muskuli", "M. coracobrachialis", "coracobrachialis",
                     """
<b>Boshlanishi:</b> kurakning tumshuqsimon o'simtasi
<b>Birikishi:</b> yelka suyagining o'rta qismi ichki yuzasi
<b>Vazifasi:</b> qo'lni oldinga ko'tarish va tanaga yaqinlashtirish
<b>Nervi:</b> mushak-teri nervi (uni teshib o'tadi)
"""),
                item("triceps", "Yelkaning uch boshli muskuli", "M. triceps brachii", "triceps brachii",
                     """
<b>Boshlanishi:</b> 3 boshcha —
• Uzun: kurakning bo'g'im osti do'mbog'i
• Lateral va medial: yelka suyagining orqa yuzasi
<b>Birikishi:</b> tirsak suyagining tirsak o'simtasi (olecranon)
<b>Vazifasi:</b> tirsakni <b>yozish</b> (bicepsga antagonist)
<b>Nervi:</b> bilak nervi (radialis)

💡 Yelka muskul massasining ~2/3 qismi — tricepsda, bicepsda emas!
"""),
            ],
        ),
        category(
            "forearm",
            "✋ Bilak va kaft muskullari",
            "Bilakda <b>20 ga yaqin</b>, kaftda <b>~19 ta</b> muskul bor — ular barmoqlarning nozik harakatlarini ta'minlaydi.",
            [
                item("brachiorad", "Yelka-bilak muskuli", "M. brachioradialis", "brachioradialis",
                     """
<b>Boshlanishi:</b> yelka suyagining pastki tashqi qirrasi
<b>Birikishi:</b> bilak (radius) suyagining bigizsimon o'simtasi
<b>Vazifasi:</b> tirsakni bukish (ayniqsa bilak o'rta holatda — stakanni ko'targanda)
<b>Nervi:</b> bilak nervi
"""),
                item("flexors", "Bilak bukuvchi muskullari", "Mm. flexores antebrachii", "forearm flexor muscles",
                     """
<b>Joylashuvi:</b> bilakning old (kaft) tomonida; ko'pchiligi yelka suyagining ichki do'ngchasidan boshlanadi

<b>Asosiylari:</b>
• Kaftni bilak tomonga bukuvchi (flexor carpi radialis)
• Kaftni tirsak tomonga bukuvchi (flexor carpi ulnaris)
• Uzun kaft muskuli (har 7 kishidan 1 tasida bo'lmaydi!)
• Barmoqlarni yuza va chuqur bukuvchilar
• Bosh barmoqni uzun bukuvchi
• Yumaloq pronator — kaftni pastga burish

<b>Nervi:</b> asosan o'rta nerv, qisman tirsak nervi
""", q="flexor digitorum superficialis"),
                item("extensors", "Bilak yozuvchi muskullari", "Mm. extensores antebrachii", "forearm extensor muscles",
                     """
<b>Joylashuvi:</b> bilakning orqa tomonida; ko'pchiligi yelka suyagining tashqi do'ngchasidan boshlanadi

<b>Asosiylari:</b>
• Kaftni uzun va kalta bilak tomonga yozuvchilar
• Kaftni tirsak tomonga yozuvchi
• Barmoqlarni yozuvchi muskul
• Bosh barmoqni uzoqlashtiruvchi va yozuvchilar
• Supinator — kaftni yuqoriga burish

<b>Nervi:</b> bilak nervi (radialis)
⚠️ <i>"Tennischi tirsagi"</i> — shu muskullar payining yallig'lanishi.
""", q="extensor digitorum"),
                item("handm", "Kaft muskullari", "Mm. manus", "hand muscles",
                     """
<b>3 guruh:</b>
• <b>Bosh barmoq tepaligi</b> (tenar) — 4 muskul: bosh barmoqni boshqa barmoqlarga qarama-qarshi qo'yish (ushlash!)
• <b>Jimjiloq tepaligi</b> (gipotenar) — 4 muskul
• <b>O'rta guruh</b> — chuvalchangsimon (4) va suyaklararo (7) muskullar: barmoqlarni yoyish, yig'ish

<b>Nervi:</b> o'rta va tirsak nervlari

💡 Bosh barmoqning qarama-qarshi qo'yilishi — odamni boshqa hayvonlardan ajratib turuvchi muhim xususiyat.
""", q="thenar muscles"),
            ],
        ),
        category(
            "hip",
            "🍑 Chanoq va son muskullari",
            "Bu muskullar tanani tik tutadi, yurish, yugurish va sakrashni ta'minlaydi — tanadagi eng kuchli muskullar.",
            [
                item("glutmax", "Katta dumba muskuli", "M. gluteus maximus", "gluteus maximus",
                     """
<b>Boshlanishi:</b> yonbosh suyagi orqa qismi, dumg'aza, dum suyagi
<b>Birikishi:</b> son suyagining dumba g'adir-budurligi, yonbosh-katta boldir yo'li
<b>Vazifasi:</b> sonni yozish (o'tirgan joydan turish, zinaga chiqish, yugurish), tanani tik tutish
<b>Nervi:</b> pastki dumba nervi

💡 Tanadagi <b>eng katta</b> va eng og'ir muskul.
"""),
                item("glutmed", "O'rta va kichik dumba muskullari", "Mm. gluteus medius et minimus", "gluteus medius",
                     """
<b>Joylashuvi:</b> katta dumba muskuli ostida
<b>Boshlanishi:</b> yonbosh suyagining tashqi yuzasi
<b>Birikishi:</b> son suyagining katta ko'sti
<b>Vazifasi:</b> sonni yon tomonga uzoqlashtirish; <b>bir oyoqda turganda chanoqni tekis ushlab turish</b>
<b>Nervi:</b> yuqori dumba nervi

⚠️ Kuchsiz bo'lsa — yurganda chanoq qiyshayadi (Trendelenburg belgisi).
"""),
                item("iliopsoas", "Yonbosh-bel muskuli", "M. iliopsoas", "iliopsoas",
                     """
<b>2 qismi:</b>
• Katta bel muskuli — bel umurtqalaridan boshlanadi
• Yonbosh muskuli — yonbosh chuqurchasidan
<b>Birikishi:</b> son suyagining kichik ko'sti
<b>Vazifasi:</b> sonni bukishning <b>eng kuchli</b> muskuli (oyoqni ko'tarish, yotgan joydan o'tirish)
<b>Nervi:</b> son nervi va bel chigali shoxlari
"""),
                item("quadriceps", "Sonning to'rt boshli muskuli", "M. quadriceps femoris", "quadriceps femoris",
                     """
<b>4 boshchasi:</b>
• To'g'ri muskul (yonbosh suyagidan)
• Lateral keng muskul
• Medial keng muskul
• Oraliq keng muskul
<b>Birikishi:</b> umumiy pay orqali tizza qopqog'i va katta boldir suyagi do'mbog'iga
<b>Vazifasi:</b> tizzani <b>yozish</b> (yurish, sakrash, to'pni tepish)
<b>Nervi:</b> son nervi

💡 Tanadagi eng kuchli muskullardan biri.
"""),
                item("sartorius", "Tikuvchi muskul", "M. sartorius", "sartorius",
                     """
<b>Boshlanishi:</b> yonbosh suyagining oldingi yuqori qirrasi
<b>Birikishi:</b> katta boldir suyagining ichki yuzasi
<b>Vazifasi:</b> sonni va tizzani bukish, sonni tashqariga burish ("chordana qurib o'tirish" holati)
<b>Nervi:</b> son nervi

💡 Tanadagi <b>eng uzun muskul</b> (~50 sm). Nomi tikuvchilar o'tirish holatidan olingan.
"""),
                item("hamstrings", "Sonning orqa muskullari", "Mm. biceps femoris, semitendinosus, semimembranosus", "hamstring muscles",
                     """
<b>3 ta muskul:</b>
• <b>Sonning ikki boshli muskuli</b> — tashqi tomonda
• <b>Yarim payli muskul</b> — ichki tomonda
• <b>Yarim pardali muskul</b> — ichki tomonda, chuqurroq
<b>Boshlanishi:</b> quymich suyagi do'mbog'i
<b>Vazifasi:</b> tizzani bukish, sonni orqaga yozish
<b>Nervi:</b> quymich nervi

⚠️ Sprinterlarda (tez yuguruvchilarda) cho'zilishi ko'p uchraydi.
""", q="hamstring"),
                item("adductors", "Sonni yaqinlashtiruvchi muskullar", "Mm. adductores", "adductor muscles",
                     """
<b>Joylashuvi:</b> sonning ichki tomonida
<b>Tarkibi:</b> uzun, kalta, katta yaqinlashtiruvchi muskullar, taroqsimon va nozik muskullar
<b>Boshlanishi:</b> qov va quymich suyaklari
<b>Birikishi:</b> son suyagining orqa qirrasi
<b>Vazifasi:</b> oyoqlarni bir-biriga yaqinlashtirish (otda o'tirish, futbolda to'pni ichki tomon bilan tepish)
<b>Nervi:</b> yopqich nerv
""", q="adductor longus"),
            ],
        ),
        category(
            "calf",
            "🦶 Boldir va oyoq panjasi muskullari",
            "Boldir muskullari oyoq panjasini harakatlantiradi va yurishda tanani oldinga itaradi.",
            [
                item("gastroc", "Boldir muskuli", "M. gastrocnemius", "gastrocnemius",
                     """
<b>Boshlanishi:</b> 2 boshcha — son suyagining ichki va tashqi do'ngchalari
<b>Birikishi:</b> <b>Axill payi</b> orqali tovon suyagi do'mbog'iga
<b>Vazifasi:</b> oyoq uchida turish, sakrash, tizzani bukishga yordam
<b>Nervi:</b> katta boldir nervi

💡 Boldirning ko'rinadigan "baliqchasi" — aynan shu muskul.
"""),
                item("soleus", "Kambalasimon muskul", "M. soleus", "soleus",
                     """
<b>Joylashuvi:</b> boldir muskuli ostida
<b>Boshlanishi:</b> katta va kichik boldir suyaklarining orqa yuzasi
<b>Birikishi:</b> Axill payi orqali tovon suyagiga
<b>Vazifasi:</b> tik turganda tanani yiqilishdan saqlash, oyoq uchida turish

💡 "Ikkinchi yurak" deb ataladi — qisqarganda venoz qonni yurakka haydaydi.
Boldir muskuli + kambalasimon = <b>boldirning uch boshli muskuli</b>.
"""),
                item("achilles", "Axill payi", "Tendo calcaneus", "achilles tendon",
                     """
<b>Joylashuvi:</b> boldirning pastki orqa qismi, tovon suyagiga birikadi
<b>Uzunligi:</b> ~15 sm
<b>Vazifasi:</b> boldir muskullari kuchini tovonga uzatish

💡 Tanadagi <b>eng kuchli va eng yo'g'on pay</b> — yugurganda tana vaznidan 8–12 marta ko'p yukni ko'taradi.
Nomi yunon afsonasidagi qahramon Axillesdan olingan.
""", q="calcaneal tendon"),
                item("tibant", "Oldingi katta boldir muskuli", "M. tibialis anterior", "tibialis anterior",
                     """
<b>Joylashuvi:</b> boldirning old yuzasida, katta boldir suyagi yonida
<b>Boshlanishi:</b> katta boldir suyagining tashqi yuzasi
<b>Birikishi:</b> ichki ponasimon suyak, I oyoq kafti suyagi
<b>Vazifasi:</b> oyoq panjasini yuqoriga ko'tarish (tovonda yurish), ichkariga burish
<b>Nervi:</b> chuqur kichik boldir nervi
"""),
                item("fibularis", "Kichik boldir muskullari", "Mm. fibulares (peronei) longus et brevis", "fibularis longus",
                     """
<b>Joylashuvi:</b> boldirning tashqi yuzasida
<b>Boshlanishi:</b> kichik boldir suyagi
<b>Birikishi:</b> uzuni — oyoq tagidan o'tib I oyoq kafti suyagiga; kaltasi — V oyoq kafti suyagiga
<b>Vazifasi:</b> oyoq panjasini tashqariga burish, oyoq gumbazini ushlab turish
<b>Nervi:</b> yuza kichik boldir nervi

⚠️ To'piq "qayrilishi"da ko'pincha shikastlanadi.
"""),
                item("footm", "Oyoq panjasi muskullari", "Mm. pedis", "foot muscles",
                     """
<b>Oyoq ustidagi muskullar:</b> barmoqlarni kalta yozuvchi muskullar
<b>Oyoq tagidagi muskullar (4 qavat):</b>
• Barmoqlarni kalta bukuvchi
• Bosh barmoqni va jimjiloqni uzoqlashtiruvchi
• Kvadrat muskul, chuvalchangsimon muskullar
• Suyaklararo muskullar

<b>Vazifasi:</b> oyoq <b>gumbazini</b> (tovon va barmoqlar orasidagi ravoq) ushlab turish, yurishda tayanch.
⚠️ Gumbaz pasaysa — <i>yassi oyoqlik</i>.
""", q="flexor digitorum brevis"),
            ],
        ),
    ],
)
