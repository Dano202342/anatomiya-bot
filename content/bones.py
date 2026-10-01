from .common import category, item, section

BONES = section(
    "suyak",
    "🦴 Suyaklar va bo'g'imlar",
    """
<b>🦴 SKELET TIZIMI</b>

Katta yoshli odamda <b>206 ta</b> suyak bor (yangi tug'ilgan chaqaloqda ~270–300 ta — o'sish davomida ko'plari qo'shilib ketadi).
Skelet tana vaznining <b>~15%</b> ini tashkil etadi. Tanada <b>~360 ta</b> bo'g'in (suyaklar birikmasi) bor.

<b>📊 Suyaklar soni hududlar bo'yicha:</b>
• Kalla — <b>22</b> (miya qismi 8 + yuz qismi 14)
• Eshitish suyakchalari — <b>6</b>
• Til osti suyagi — <b>1</b>
• Umurtqa pog'onasi — <b>26</b>
• Ko'krak qafasi — <b>25</b> (to'sh 1 + qovurg'a 24)
• Yelka kamari va qo'llar — <b>64</b>
• Chanoq kamari va oyoqlar — <b>62</b>
━━━━━━━━━━━━━━
<b>Jami: 206</b>

Bo'limni tanlang 👇
""",
    [
        category(
            "general",
            "📚 Umumiy ma'lumot",
            "Suyak qanday tuzilgan, qanday turlari va bo'g'imlar qanday bo'ladi.",
            [
                item("bonestruct", "Suyak tuzilishi", "Os", "bone structure",
                     """
<b>Suyak qavatlari (tashqaridan ichkariga):</b>
• <b>Suyak usti pardasi (periost)</b> — qon tomir va nervlarga boy; suyakni o'stiradi va sinsa tiklaydi
• <b>Zich (kompakt) modda</b> — qattiq, mustahkam tashqi qatlam
• <b>G'ovak (spongioz) modda</b> — to'rsimon, yengil; suyak uchlarida
• <b>Suyak ko'migi</b>:
  – <i>Qizil ko'mik</i> — qon hujayralarini ishlab chiqaradi (sekundiga ~2 mln eritrotsit!)
  – <i>Sariq ko'mik</i> — yog' to'qimasi

<b>Kimyoviy tarkibi:</b> ~2/3 mineral (kalsiy fosfat — qattiqlik), ~1/3 organik (kollagen — egiluvchanlik).

💡 Suyak bir xil og'irlikdagi po'latdan mustahkamroq!
"""),
                item("bonetypes", "Suyak turlari", "Classificatio ossium", "bone types",
                     """
<b>Shakliga ko'ra 5 tur:</b>
• 🦴 <b>Uzun (naysimon)</b> — son, yelka, boldir suyaklari, falangalar
• 🎲 <b>Kalta</b> — kaft usti, oyoq kaft usti suyaklari
• 📄 <b>Yassi</b> — kalla gumbazi, to'sh, qovurg'alar, kurak
• 🧩 <b>Noto'g'ri shakldagi</b> — umurtqalar, ponasimon suyak, yuz suyaklari
• 🌰 <b>Sesamasimon</b> — pay ichidagi suyaklar (tizza qopqog'i, no'xatsimon suyak)

<b>Uzun suyak qismlari:</b>
• Diafiz — tanasi (o'rta qismi)
• Epifizlar — ikki uchi (bo'g'im yuzalari)
• Metafiz — o'sish zonasi (o'sish plastinkasi)
"""),
                item("jointtypes", "Bo'g'im turlari", "Juncturae ossium", "synovial joint",
                     """
<b>Suyaklar birikishining 3 turi:</b>

🔒 <b>Fibroz (harakatsiz)</b> — biriktiruvchi to'qima orqali: kalla <b>choklari</b>, tish-jag' birikmasi
🔗 <b>Tog'ayli (kam harakatli)</b> — umurtqalararo disklar, qov simfizi
🔄 <b>Sinovial (harakatchan) — haqiqiy bo'g'imlar</b>

<b>Sinovial bo'g'im tuzilishi:</b> bo'g'im yuzalari (gialin tog'ay bilan qoplangan), bo'g'im kapsulasi, bo'g'im bo'shlig'i, sinovial suyuqlik ("moy").

<b>Sinovial bo'g'imlarning 6 shakli:</b>
• <b>Sharsimon</b> — har tomonga: yelka, son-chanoq
• <b>G'altaksimon (blokli)</b> — bir tekislikda: tirsak, barmoqlararo
• <b>Egarsimon</b> — bosh barmoq asosi
• <b>Ellipssimon</b> — bilak-kaft usti
• <b>Silindrsimon (aylanma)</b> — atlant-aksis, bilak-tirsak
• <b>Yassi</b> — umurtqa o'simtalari orasida, kaft usti suyaklari orasida
"""),
            ],
        ),
        category(
            "skull",
            "💀 Kalla suyaklari (22)",
            """
Kalla <b>22 ta</b> suyakdan iborat:
• <b>Miya qismi</b> — 8 ta (miyani himoya qiladi)
• <b>Yuz qismi</b> — 14 ta

Kalla suyaklari bir-biri bilan <b>choklar</b> orqali harakatsiz birikkan.
Yagona harakatchan bo'g'im — <b>chakka-pastki jag' bo'g'imi</b>.
""",
            [
                item("frontal", "Peshona suyagi (1 ta)", "Os frontale", "frontal bone",
                     """
<b>Soni:</b> 1 ta (toq)
<b>Joylashuvi:</b> kallaning old qismi — peshona va ko'z kosalarining yuqori devori
<b>Ichida:</b> peshona bo'shlig'i (sinus) — havo bilan to'la

<b>Birikadi (choklar):</b>
• Tepa suyaklari bilan — <b>toj chok</b>
• Burun, ko'z yosh, g'alvirsimon, ponasimon, yonoq va yuqori jag' suyaklari bilan

💡 Chaqaloqda 2 ta bo'ladi, 2 yoshgacha qo'shilib ketadi.
"""),
                item("parietal", "Tepa suyaklari (2 ta)", "Os parietale", "parietal bone",
                     """
<b>Soni:</b> 2 ta (juft)
<b>Joylashuvi:</b> kallaning yuqori va yon devorlari (gumbazi)
<b>Shakli:</b> to'rtburchak, qavariq yassi suyak

<b>Birikadi (choklar):</b>
• Bir-biri bilan — <b>sagittal (o'qsimon) chok</b>
• Peshona suyagi bilan — <b>toj chok</b>
• Ensa suyagi bilan — <b>lambdasimon chok</b>
• Chakka suyagi bilan — <b>tangachali chok</b>

💡 Chaqaloqda bu suyaklar orasida yumshoq <b>liqildoqlar</b> bo'ladi (katta liqildoq 1–1,5 yoshda yopiladi).
"""),
                item("temporal", "Chakka suyaklari (2 ta)", "Os temporale", "temporal bone",
                     """
<b>Soni:</b> 2 ta (juft)
<b>Joylashuvi:</b> kallaning yon pastki qismi, quloq atrofida

<b>Qismlari:</b>
• Tangachali qism
• <b>Toshsimon qism (piramida)</b> — tanadagi <u>eng qattiq</u> suyak qismi; ichida o'rta va ichki quloq
• So'rg'ichsimon o'simta (quloq orqasida seziladi)
• Bigizsimon o'simta, yonoq o'simtasi

<b>Bo'g'imlari:</b>
• Pastki jag' bilan — <b>chakka-pastki jag' bo'g'imi</b> (kallaning yagona harakatchan bo'g'imi)
• Tepa, ensa, ponasimon, yonoq suyaklari bilan — choklar
"""),
                item("occipital", "Ensa suyagi (1 ta)", "Os occipitale", "occipital bone",
                     """
<b>Soni:</b> 1 ta (toq)
<b>Joylashuvi:</b> kallaning orqa va pastki qismi
<b>Muhim tuzilmasi:</b> <b>katta ensa teshigi</b> — u orqali orqa miya bosh miyaga ulanadi

<b>Bo'g'imlari:</b>
• I bo'yin umurtqasi (atlant) bilan — <b>atlant-ensa bo'g'imi</b> (ellipssimon; "ha" deb bosh qimirlatish)
• Tepa suyaklari bilan — lambdasimon chok
• Chakka va ponasimon suyaklar bilan
"""),
                item("sphenoid", "Ponasimon suyak (1 ta)", "Os sphenoidale", "sphenoid bone",
                     """
<b>Soni:</b> 1 ta (toq)
<b>Joylashuvi:</b> kalla asosining markazida — barcha miya suyaklari bilan tutashadi
<b>Shakli:</b> uchayotgan ko'rshapalak yoki kapalakka o'xshaydi

<b>Qismlari:</b> tana (ichida <b>turk egari</b> — gipofiz bezi joylashadi), katta va kichik qanotlar, qanotsimon o'simtalar.

<b>Birikadi:</b> barcha 7 ta miya suyagi + bir qancha yuz suyaklari bilan (12 ta suyak bilan).
💡 "Kallaning kalit toshi" deb ataladi.
"""),
                item("ethmoid", "G'alvirsimon suyak (1 ta)", "Os ethmoidale", "ethmoid bone",
                     """
<b>Soni:</b> 1 ta (toq)
<b>Joylashuvi:</b> ko'z kosalari orasida, burun bo'shlig'ining yuqori qismida
<b>Xususiyati:</b> juda yengil, g'ovak suyak

<b>Qismlari:</b>
• <b>G'alvirsimon plastinka</b> — teshikchalari orqali hid bilish nervlari o'tadi
• Perpendikulyar plastinka — burun to'sig'ining bir qismi
• Labirintlar — havo yacheykalari; yuqori va o'rta burun chig'anoqlari
"""),
            ],
        ),
        category(
            "face",
            "🙂 Yuz suyaklari (14)",
            "Yuz skeletini <b>14 ta</b> suyak hosil qiladi: 6 juft + 2 toq.",
            [
                item("maxilla", "Yuqori jag' suyagi (2 ta)", "Maxilla", "maxilla",
                     """
<b>Soni:</b> 2 ta (juft, o'rtada qo'shilgan)
<b>Joylashuvi:</b> yuzning markazi — yuqori tishlar, qattiq tanglay, burun va ko'z kosasi devorlari
<b>Ichida:</b> <b>yuqori jag' (Gaymor) bo'shlig'i</b> — eng katta havo bo'shlig'i (yallig'lanishi — gaymorit)

<b>Birikadi:</b> barcha yuz suyaklari (pastki jag'dan tashqari) va peshona, g'alvirsimon suyaklar bilan.
<b>Tishlar:</b> 16 ta yuqori tish shu suyakda.
"""),
                item("mandible", "Pastki jag' suyagi (1 ta)", "Mandibula", "mandible",
                     """
<b>Soni:</b> 1 ta (toq)
<b>Xususiyati:</b> yuzning <b>eng katta va eng mustahkam</b> suyagi; kallaning <b>yagona harakatchan</b> suyagi

<b>Qismlari:</b> tanasi (16 ta pastki tish), ikki shoxi, toj o'simtasi, bo'g'im o'simtasi, iyak do'mbog'i

<b>Bo'g'imi:</b> <b>chakka-pastki jag' bo'g'imi</b> (2 ta, o'ng va chap) — ichida tog'ay disk bor; og'izni ochish, chaynash, jag'ni yonga va oldinga surish imkonini beradi.
"""),
                item("zygomatic_b", "Yonoq suyagi (2 ta)", "Os zygomaticum", "zygomatic bone",
                     """
<b>Soni:</b> 2 ta (juft)
<b>Joylashuvi:</b> yuzning yon tomonida, yonoq do'mbog'ini hosil qiladi
<b>Birikadi:</b> peshona, chakka, yuqori jag' va ponasimon suyaklar bilan
• Chakka suyagi bilan birgalikda <b>yonoq ravog'ini</b> hosil qiladi

💡 Yonoq ravog'iga chaynov muskuli birikadi.
"""),
                item("nasal", "Burun suyagi (2 ta)", "Os nasale", "nasal bone",
                     """
<b>Soni:</b> 2 ta (juft)
<b>Joylashuvi:</b> burun qirrasining yuqori qismi ("burun ko'prigi")
<b>O'lchami:</b> kichik, to'rtburchak

<b>Birikadi:</b> bir-biri bilan, peshona suyagi va yuqori jag' bilan.
Burunning pastki qismi — tog'aydan iborat.
⚠️ Yuz suyaklari ichida eng ko'p sinadigani.
"""),
                item("lacrimal", "Ko'z yosh suyagi (2 ta)", "Os lacrimale", "lacrimal bone",
                     """
<b>Soni:</b> 2 ta (juft)
<b>Joylashuvi:</b> ko'z kosasining ichki devori
<b>Xususiyati:</b> yuzning <b>eng kichik va eng nozik</b> suyagi (tirnoqdek)

<b>Vazifasi:</b> ko'z yoshi xaltasi chuqurchasini hosil qiladi — ko'z yoshi shu yerdan burunga oqib tushadi.
"""),
                item("palatine", "Tanglay suyagi (2 ta)", "Os palatinum", "palatine bone",
                     """
<b>Soni:</b> 2 ta (juft)
<b>Joylashuvi:</b> og'iz bo'shlig'ining orqa yuqori qismi
<b>Shakli:</b> "L" harfiga o'xshaydi

<b>Vazifasi:</b> qattiq tanglayning orqa 1/3 qismini, burun bo'shlig'i va ko'z kosasi devorining bir qismini hosil qiladi.
"""),
                item("concha", "Pastki burun chig'anog'i (2 ta)", "Concha nasalis inferior", "inferior nasal concha",
                     """
<b>Soni:</b> 2 ta (juft)
<b>Joylashuvi:</b> burun bo'shlig'ining yon devorida
<b>Xususiyati:</b> mustaqil suyak (yuqori va o'rta chig'anoqlar esa g'alvirsimon suyakning qismi)

<b>Vazifasi:</b> nafas olingan havoni isitish, namlash va changdan tozalash.
"""),
                item("vomer", "Dimog' suyagi (1 ta)", "Vomer", "vomer",
                     """
<b>Soni:</b> 1 ta (toq)
<b>Joylashuvi:</b> burun to'sig'ining pastki-orqa qismi
<b>Shakli:</b> yupqa, plug tishiga (omoch) o'xshaydi

<b>Vazifasi:</b> burun bo'shlig'ini o'ng va chap yarmiga ajratadi (g'alvirsimon suyakning perpendikulyar plastinkasi va tog'ay bilan birga).
"""),
            ],
        ),
        category(
            "ear",
            "👂 Eshitish suyakchalari va til osti",
            "O'rta quloqdagi <b>6 ta</b> eng kichik suyak va hech bir suyakka birikmagan <b>til osti suyagi</b>.",
            [
                item("ossicles", "Eshitish suyakchalari (6 ta)", "Ossicula auditus", "ossicles",
                     """
<b>Soni:</b> har bir quloqda 3 tadan = <b>6 ta</b>
<b>Joylashuvi:</b> o'rta quloq (nog'ora bo'shlig'i), chakka suyagi ichida

<b>3 ta suyakcha:</b>
• 🔨 <b>Bolg'acha</b> (malleus) — nog'ora pardaga birikkan
• ⚒ <b>Sandon</b> (incus) — o'rtada
• 🏇 <b>Uzangi</b> (stapes) — ichki quloq dahliz darchasiga birikkan

<b>Bo'g'imlari:</b> bolg'acha-sandon va sandon-uzangi bo'g'imlari (sinovial!)
<b>Vazifasi:</b> nog'ora parda tebranishini ~20 marta kuchaytirib ichki quloqqa uzatish.

💡 <b>Uzangi — tanadagi eng kichik suyak</b> (~3 mm, 3 mg)!
""", q="auditory ossicles"),
                item("hyoidb", "Til osti suyagi (1 ta)", "Os hyoideum", "hyoid bone",
                     """
<b>Soni:</b> 1 ta (toq)
<b>Joylashuvi:</b> bo'yinning old qismida, pastki jag' va hiqildoq orasida
<b>Shakli:</b> taqa ("U") shaklida — tana, katta va kichik shoxlar

💡 Tanadagi <b>hech bir suyak bilan bo'g'im hosil qilmaydigan yagona suyak</b> — faqat muskul va boylamlar bilan "osilib" turadi.

<b>Vazifasi:</b> til va bo'yin muskullari uchun tayanch; yutish va gapirishda qatnashadi.
"""),
            ],
        ),
        category(
            "spine",
            "🐍 Umurtqa pog'onasi (26)",
            """
Umurtqa pog'onasi kattalarda <b>26 ta</b> suyakdan iborat (bolalarda 33–34 ta umurtqa):
• Bo'yin — 7 ta
• Ko'krak — 12 ta
• Bel — 5 ta
• Dumg'aza — 1 ta (5 ta qo'shilgan umurtqa)
• Dum — 1 ta (3–5 ta qo'shilgan umurtqa)

<b>4 ta fiziologik egrilik:</b> bo'yin va bel lordozi (oldinga), ko'krak va dumg'aza kifozi (orqaga) — "prujina" vazifasini bajaradi.
""",
            [
                item("vertebra", "Umurtqa tuzilishi va bo'g'imlari", "Vertebra", "vertebra",
                     """
<b>Tipik umurtqa qismlari:</b>
• <b>Tana</b> — old qismi, og'irlikni ko'taradi
• <b>Ravoq</b> — orqa qismi; tana bilan birga <b>umurtqa teshigini</b> hosil qiladi (orqa miya o'tadi)
• <b>7 ta o'simta:</b> 1 o'tkir (orqada seziladi), 2 ko'ndalang, 4 bo'g'im o'simtasi

<b>Umurtqalar birikishi:</b>
• <b>Umurtqalararo disklar</b> — <b>23 ta</b> tog'ay "yostiqcha" (ichida pulpoz yadro); umurtqa pog'onasi uzunligining ~25% i
• <b>Fasetka (bo'g'im o'simtalari) bo'g'imlari</b> — yassi sinovial bo'g'imlar
• Boylamlar: oldingi va orqa bo'ylama, sariq boylam va b.

⚠️ Disk tashqariga chiqishi — <i>churra (grija)</i>.
"""),
                item("cervical", "Bo'yin umurtqalari (7 ta)", "Vertebrae cervicales C1–C7", "cervical vertebrae",
                     """
<b>Soni:</b> 7 ta (C1–C7) — deyarli barcha sutemizuvchilarda ham 7 ta (jirafada ham!)
<b>Xususiyati:</b> eng kichik va eng harakatchan umurtqalar; ko'ndalang o'simtalarida teshik bor (umurtqa arteriyasi o'tadi)

<b>Maxsus umurtqalar:</b>
• <b>C1 — Atlant</b>: tanasi yo'q, halqa shaklida; boshni ko'tarib turadi
• <b>C2 — Aksis (o'q)</b>: tish o'simtasi bor, atlant uning atrofida aylanadi
• <b>C7 — Turtib chiqqan umurtqa</b>: o'tkir o'simtasi bo'yin pastida yaqqol seziladi

<b>Bo'g'imlari:</b>
• Atlant-ensa bo'g'imi — boshni oldinga-orqaga egish ("ha")
• <b>Atlant-aksis bo'g'imi</b> — boshni burish ("yo'q"), silindrsimon
"""),
                item("thoracic", "Ko'krak umurtqalari (12 ta)", "Vertebrae thoracicae T1–T12", "thoracic vertebrae",
                     """
<b>Soni:</b> 12 ta (T1–T12)
<b>Xususiyati:</b> qovurg'alar bilan birikadi; o'tkir o'simtalari uzun va pastga qiya (cherepitsadek)

<b>Bo'g'imlari:</b>
• <b>Qovurg'a boshchasi bo'g'imi</b> — umurtqa tanasi bilan
• <b>Qovurg'a-ko'ndalang o'simta bo'g'imi</b> — ko'ndalang o'simta bilan
• Har bir umurtqa 2 tomondan qovurg'alar bilan → jami ~<b>48 ta</b> qovurg'a-umurtqa bo'g'imi

💡 Ko'krak qafasi tufayli eng kam harakatchan qism.
"""),
                item("lumbar", "Bel umurtqalari (5 ta)", "Vertebrae lumbales L1–L5", "lumbar vertebrae",
                     """
<b>Soni:</b> 5 ta (L1–L5)
<b>Xususiyati:</b> eng <b>katta va massiv</b> umurtqalar — tana og'irligining ko'p qismini ko'taradi

<b>Bo'g'imlari:</b>
• Bir-biri bilan disklar va fasetka bo'g'imlari orqali
• L5 — dumg'aza bilan (<b>bel-dumg'aza birikmasi</b>)

⚠️ Eng ko'p og'riydigan va churra hosil bo'ladigan joy — L4–L5 va L5–S1 disklari.
"""),
                item("sacrum", "Dumg'aza va dum suyagi", "Os sacrum et os coccygis", "sacrum",
                     """
<b>🔺 Dumg'aza suyagi (1 ta)</b>
• 5 ta umurtqaning (S1–S5) <b>qo'shilishidan</b> hosil bo'ladi (16–25 yoshda)
• Uchburchak shaklda; 4 juft teshigidan dumg'aza nervlari chiqadi
• <b>Bo'g'imlari:</b> L5 bilan; ikki tomonda chanoq suyaklari bilan — <b>dumg'aza-yonbosh bo'g'imlari</b> (2 ta, kam harakatli); dum suyagi bilan

<b>🔻 Dum suyagi (1 ta)</b>
• 3–5 ta kichik umurtqaning qo'shilishidan iborat
• Odamdagi "dum qoldig'i"
• Ko'plab muskul va boylamlar birikadi
""", q="sacrum coccyx"),
            ],
        ),
        category(
            "thorax",
            "🫁 Ko'krak qafasi (25)",
            "Ko'krak qafasi <b>12 ta</b> ko'krak umurtqasi, <b>24 ta</b> qovurg'a va <b>1 ta</b> to'sh suyagidan iborat. Yurak va o'pkani himoya qiladi.",
            [
                item("sternum", "To'sh suyagi (1 ta)", "Sternum", "sternum",
                     """
<b>Soni:</b> 1 ta (toq)
<b>Joylashuvi:</b> ko'krak qafasining old markazida
<b>Shakli:</b> xanjar (qilich) shaklida, uzunligi ~15–20 sm

<b>3 qismi:</b>
• <b>Dasta</b> (yuqori qismi)
• <b>Tana</b> (o'rta, eng uzun qismi)
• <b>Xanjarsimon o'simta</b> (pastki uchi, 40 yoshgacha tog'ay)

<b>Bo'g'imlari:</b>
• O'mrov suyaklari bilan — <b>to'sh-o'mrov bo'g'imi</b> (2 ta) — qo'lning tanaga yagona suyak birikmasi!
• I–VII qovurg'a tog'aylari bilan — <b>to'sh-qovurg'a bo'g'imlari</b> (14 ta)
"""),
                item("ribs", "Qovurg'alar (24 ta)", "Costae", "rib cage",
                     """
<b>Soni:</b> 12 juft = <b>24 ta</b> (erkak va ayolda bir xil!)

<b>Turlari:</b>
• <b>Chin qovurg'alar</b> (I–VII juft) — to'g'ridan-to'g'ri to'sh suyagiga birikadi
• <b>Soxta qovurg'alar</b> (VIII–X juft) — tog'aylari yuqoridagi qovurg'a tog'ayiga birikadi
• <b>Erkin (tebranuvchi) qovurg'alar</b> (XI–XII juft) — old uchi erkin, qorin muskullarida tugaydi

<b>Har bir qovurg'aning bo'g'imlari:</b>
• Orqada — umurtqa tanasi va ko'ndalang o'simtasi bilan (2 ta bo'g'im)
• Oldinda — tog'ay orqali to'sh suyagi bilan

💡 Nafas olganda qovurg'alar "chelak dastasi" kabi yuqoriga ko'tariladi.
""", q="rib"),
            ],
        ),
        category(
            "upper",
            "💪 Yelka kamari va qo'l (64)",
            """
Har bir qo'lda <b>32 ta</b> suyak, jami <b>64 ta</b>:
• O'mrov — 2
• Kurak — 2
• Yelka suyagi — 2
• Bilak (radius) — 2
• Tirsak suyagi (ulna) — 2
• Kaft usti — 16
• Kaft — 10
• Barmoq falangalari — 28
""",
            [
                item("clavicle", "O'mrov suyagi (2 ta)", "Clavicula", "clavicle",
                     """
<b>Soni:</b> 2 ta
<b>Joylashuvi:</b> bo'yin va ko'krak chegarasida, gorizontal; teri ostida yaqqol seziladi
<b>Shakli:</b> "S" harfiga o'xshash

<b>Bo'g'imlari:</b>
• Ichki uchi — to'sh suyagi bilan: <b>to'sh-o'mrov bo'g'imi</b>
• Tashqi uchi — kurakning yelka o'simtasi bilan: <b>yelka o'simtasi-o'mrov bo'g'imi</b>

💡 Ona qornida <b>birinchi</b> suyaklanadigan suyak; eng ko'p sinadigan suyaklardan biri (qo'lga yiqilganda).
"""),
                item("scapula", "Kurak (2 ta)", "Scapula", "scapula",
                     """
<b>Soni:</b> 2 ta
<b>Joylashuvi:</b> orqaning yuqori qismida, II–VII qovurg'alar sohasida
<b>Shakli:</b> uchburchak yassi suyak

<b>Muhim qismlari:</b> kurak qirrasi, yelka o'simtasi (akromion), tumshuqsimon o'simta, <b>bo'g'im chuqurchasi</b>

<b>Bo'g'imlari:</b>
• Yelka suyagi bilan — <b>yelka bo'g'imi</b>
• O'mrov bilan — yelka o'simtasi-o'mrov bo'g'imi
• Ko'krak qafasiga suyak bilan emas, faqat <b>muskullar</b> bilan birikkan (17 ta muskul!)
"""),
                item("humerus", "Yelka suyagi (2 ta)", "Humerus", "humerus",
                     """
<b>Soni:</b> 2 ta
<b>Joylashuvi:</b> yelka (qo'lning yuqori qismi)
<b>Turi:</b> uzun naysimon suyak, uzunligi ~30–35 sm

<b>Qismlari:</b> boshcha, anatomik va jarrohlik bo'yinlar, katta va kichik do'mboqlar, tana, ichki va tashqi do'ngchalar, g'altak, boshchacha

<b>Bo'g'imlari:</b>
• Yuqorida — kurak bilan: <b>yelka bo'g'imi</b> (sharsimon)
• Pastda — tirsak va bilak suyaklari bilan: <b>tirsak bo'g'imi</b>
"""),
                item("radius", "Bilak suyagi — radius (2 ta)", "Radius", "radius bone",
                     """
<b>Soni:</b> 2 ta
<b>Joylashuvi:</b> bilakning <b>bosh barmoq tomonida</b> (tashqi tomonida)

<b>Bo'g'imlari:</b>
• Yelka suyagi bilan — tirsak bo'g'imi tarkibida
• Tirsak suyagi bilan — <b>proksimal va distal bilak-tirsak bo'g'imlari</b> (kaftni burish — pronatsiya/supinatsiya)
• Kaft usti suyaklari bilan — <b>bilak-kaft usti bo'g'imi</b>

⚠️ Pastki uchining sinishi ("tipik joyda sinish") — eng ko'p uchraydigan sinishlardan biri.
"""),
                item("ulna", "Tirsak suyagi — ulna (2 ta)", "Ulna", "ulna",
                     """
<b>Soni:</b> 2 ta
<b>Joylashuvi:</b> bilakning <b>jimjiloq tomonida</b> (ichki tomonida)

<b>Qismlari:</b> <b>tirsak o'simtasi</b> (olecranon — tirsakni tiraganda tayanadigan joy), tojsimon o'simta, g'altaksimon o'yma, bigizsimon o'simta

<b>Bo'g'imlari:</b>
• Yelka suyagi g'altagi bilan — <b>yelka-tirsak bo'g'imi</b> (g'altaksimon)
• Bilak suyagi bilan — proksimal va distal bilak-tirsak bo'g'imlari
"""),
                item("elbow", "Tirsak bo'g'imi", "Articulatio cubiti", "elbow joint",
                     """
<b>Turi:</b> <b>murakkab</b> bo'g'im — bitta kapsula ichida 3 ta bo'g'im:
1. <b>Yelka-tirsak</b> — g'altaksimon (bukish-yozish)
2. <b>Yelka-bilak</b> — sharsimon
3. <b>Proksimal bilak-tirsak</b> — silindrsimon (kaftni burish)

<b>Ishtirok etadigan suyaklar:</b> yelka, tirsak, bilak (radius)
<b>Harakatlari:</b> bukish-yozish (~0–150°), kaftni pastga-yuqoriga burish
"""),
                item("shoulder", "Yelka bo'g'imi", "Articulatio humeri", "shoulder joint",
                     """
<b>Turi:</b> <b>sharsimon</b> — tanadagi <b>eng harakatchan</b> bo'g'im
<b>Suyaklar:</b> yelka suyagi boshchasi + kurakning bo'g'im chuqurchasi

<b>Harakatlari:</b> barcha yo'nalishlarda — bukish, yozish, uzoqlashtirish, yaqinlashtirish, aylanma harakat

<b>Mustahkamlovchilar:</b> bo'g'im labi (tog'ay halqa), kapsula, <b>rotator manjeta</b> muskullari

⚠️ Erkinligi tufayli eng ko'p <b>chiqadigan</b> bo'g'im.
"""),
                item("carpals", "Kaft usti suyaklari (16 ta)", "Ossa carpi", "carpal bones",
                     """
<b>Soni:</b> har bir qo'lda 8 tadan = <b>16 ta</b>
<b>Joylashuvi:</b> bilak va kaft orasida, 2 qator bo'lib

<b>Proksimal qator (bosh barmoq tomondan):</b>
1. Qayiqsimon
2. Yarimoysimon
3. Uch qirrali
4. No'xatsimon (sesamasimon)

<b>Distal qator:</b>
5. Katta trapetsiyasimon
6. Kichik trapetsiyasimon
7. Boshchali (eng kattasi)
8. Ilmoqli

<b>Bo'g'imlari:</b> bilak suyagi bilan (bilak-kaft usti), bir-biri bilan (kaft usti suyaklararo), kaft suyaklari bilan.
⚠️ Qayiqsimon suyak — eng ko'p sinadigani.
"""),
                item("metacarpals", "Kaft suyaklari va barmoqlar (38 ta)", "Ossa metacarpi et phalanges", "metacarpal bones",
                     """
<b>✋ Kaft suyaklari:</b> har qo'lda 5 ta = <b>10 ta</b> (I–V, bosh barmoqdan boshlab)

<b>👆 Barmoq falangalari:</b> har qo'lda 14 ta = <b>28 ta</b>
• Bosh barmoqda — 2 ta (asosiy va tirnoq)
• Qolgan barmoqlarda — 3 tadan (asosiy, o'rta, tirnoq)

<b>Bo'g'imlari (har qo'lda):</b>
• <b>Bosh barmoq kaft usti-kaft bo'g'imi</b> — <b>egarsimon</b> (bosh barmoqni qarama-qarshi qo'yish!)
• Kaft-falanga bo'g'imlari — 5 ta (ellipssimon)
• Falangalararo bo'g'imlar — 9 ta (g'altaksimon)

💡 Bitta qo'l panjasida jami <b>27 ta</b> suyak bor (8+5+14).
""", q="hand bones"),
            ],
        ),
        category(
            "lower",
            "🦵 Chanoq kamari va oyoq (62)",
            """
Har bir oyoqda <b>31 ta</b> suyak, jami <b>62 ta</b>:
• Chanoq suyagi — 2
• Son suyagi — 2
• Tizza qopqog'i — 2
• Katta boldir — 2
• Kichik boldir — 2
• Oyoq kaft usti — 14
• Oyoq kafti — 10
• Barmoq falangalari — 28
""",
            [
                item("hipbone", "Chanoq suyagi (2 ta)", "Os coxae", "hip bone",
                     """
<b>Soni:</b> 2 ta
<b>Hosil bo'lishi:</b> 3 ta suyakning 16–18 yoshda <b>qo'shilishidan</b>:
• <b>Yonbosh suyagi</b> — yuqori, keng qanotli qism
• <b>Quymich suyagi</b> — pastki-orqa qism (o'tirganda tayanadi)
• <b>Qov suyagi</b> — old qism

<b>Bo'g'imlari:</b>
• Dumg'aza bilan — <b>dumg'aza-yonbosh bo'g'imi</b>
• Bir-biri bilan oldinda — <b>qov simfizi</b> (tog'ayli birikma)
• Son suyagi bilan — <b>son-chanoq bo'g'imi</b> (quymich kosachasi orqali)

💡 Ayollar chanog'i kengroq va past — tug'ruq uchun moslashgan.
"""),
                item("femur", "Son suyagi (2 ta)", "Femur", "femur",
                     """
<b>Soni:</b> 2 ta
<b>Xususiyati:</b> tanadagi <b>eng uzun, eng og'ir va eng mustahkam</b> suyak — bo'yning ~1/4 qismi (~45–50 sm)

<b>Qismlari:</b> boshcha, bo'yin, katta va kichik ko'stlar, tana, ichki va tashqi do'ngchalar

<b>Bo'g'imlari:</b>
• Yuqorida — chanoq bilan: <b>son-chanoq bo'g'imi</b>
• Pastda — katta boldir va tizza qopqog'i bilan: <b>tizza bo'g'imi</b>

💡 1 tonnagacha yukni ko'tara oladi!
⚠️ Keksalarda son suyagi bo'yni sinishi xavfli.
"""),
                item("patella", "Tizza qopqog'i (2 ta)", "Patella", "patella",
                     """
<b>Soni:</b> 2 ta
<b>Turi:</b> tanadagi <b>eng katta sesamasimon suyak</b> — to'rt boshli muskul payi ichida joylashgan
<b>Shakli:</b> uchburchak

<b>Bo'g'imi:</b> son suyagi bilan — <b>tizza qopqog'i-son bo'g'imi</b> (tizza bo'g'imi tarkibida)
<b>Vazifasi:</b> tizzani himoya qilish, to'rt boshli muskul kuchini ~30% oshirish (richag).

💡 Chaqaloqlarda tog'aydan iborat, 3–6 yoshda suyaklanadi.
"""),
                item("tibia", "Katta boldir suyagi (2 ta)", "Tibia", "tibia",
                     """
<b>Soni:</b> 2 ta
<b>Joylashuvi:</b> boldirning <b>ichki tomonida</b>; old qirrasi teri ostida seziladi
<b>Xususiyati:</b> tanadagi ikkinchi eng uzun suyak; tana og'irligining asosiy qismini ko'taradi

<b>Bo'g'imlari:</b>
• Son suyagi bilan — <b>tizza bo'g'imi</b>
• Kichik boldir bilan — yuqori va pastki boldirlararo bo'g'imlar
• Oshiq suyagi bilan — <b>boldir-oshiq (to'piq) bo'g'imi</b>; pastki uchi — <b>ichki to'piq</b>
"""),
                item("fibula", "Kichik boldir suyagi (2 ta)", "Fibula", "fibula",
                     """
<b>Soni:</b> 2 ta
<b>Joylashuvi:</b> boldirning <b>tashqi tomonida</b>
<b>Xususiyati:</b> ingichka, og'irlikni deyarli ko'tarmaydi; asosan muskullar birikishi uchun

<b>Bo'g'imlari:</b>
• Katta boldir suyagi bilan — yuqori va pastki boldirlararo bo'g'imlar
• Oshiq suyagi bilan — to'piq bo'g'imi tarkibida; pastki uchi — <b>tashqi to'piq</b>

💡 Tizza bo'g'imiga kirmaydi. Jarrohlar boshqa joylarni tiklash uchun uning bir qismini olishlari mumkin.
"""),
                item("knee", "Tizza bo'g'imi", "Articulatio genus", "knee joint",
                     """
<b>Turi:</b> tanadagi <b>eng katta va eng murakkab</b> bo'g'im (g'altaksimon-aylanma)
<b>Suyaklar:</b> son suyagi, katta boldir suyagi, tizza qopqog'i

<b>Ichki tuzilmalari:</b>
• <b>Meniskalar</b> — 2 ta yarim oy shaklidagi tog'ay (ichki va tashqi): amortizator
• <b>Xochsimon boylamlar</b> — oldingi va orqa: oldinga-orqaga siljishni oldini oladi
• Yon boylamlar — ichki va tashqi
• Sinovial xaltalar (~12 ta)

<b>Harakatlari:</b> bukish-yozish (~0–140°), bukilgan holatda biroz aylanish.
⚠️ Sportda meniskus va oldingi xochsimon boylam yirtilishi ko'p uchraydi.
"""),
                item("hipjoint", "Son-chanoq bo'g'imi", "Articulatio coxae", "hip joint",
                     """
<b>Turi:</b> <b>sharsimon</b> (yong'oqsimon) bo'g'im
<b>Suyaklar:</b> son suyagi boshchasi + chanoq suyagining quymich kosachasi

<b>Xususiyati:</b> yelka bo'g'imiga qaraganda kam harakatchan, lekin juda <b>mustahkam</b> — chuqur kosacha va tanadagi eng kuchli boylamlar (yonbosh-son boylami)

<b>Harakatlari:</b> bukish, yozish, uzoqlashtirish, yaqinlashtirish, aylantirish.
💡 Yurganda bu bo'g'imga tana og'irligidan 3–5 barobar ko'p yuk tushadi.
"""),
                item("tarsals", "Oyoq kaft usti suyaklari (14 ta)", "Ossa tarsi", "tarsal bones",
                     """
<b>Soni:</b> har oyoqda 7 tadan = <b>14 ta</b>

<b>Suyaklar:</b>
1. <b>Tovon suyagi</b> — oyoq panjasining eng katta suyagi
2. <b>Oshiq suyagi</b> — boldir suyaklari bilan bo'g'im hosil qiladi; birorta ham muskul birikmaydi!
3. Qayiqsimon suyak
4. Kubsimon suyak
5–7. <b>Uchta ponasimon suyak</b> (ichki, o'rta, tashqi)

<b>Bo'g'imlari:</b>
• <b>To'piq (boldir-oshiq) bo'g'imi</b> — g'altaksimon: panjani yuqoriga-pastga harakatlantirish
• Oshiq osti bo'g'imi — panjani ichkariga-tashqariga burish
• Kaft usti suyaklararo va kaft usti-kaft bo'g'imlari
"""),
                item("metatarsals", "Oyoq kafti va barmoq suyaklari (38 ta)", "Ossa metatarsi et phalanges", "metatarsal bones",
                     """
<b>🦶 Oyoq kafti suyaklari:</b> har oyoqda 5 ta = <b>10 ta</b> (I–V)

<b>🦶 Barmoq falangalari:</b> har oyoqda 14 ta = <b>28 ta</b>
• Bosh barmoqda — 2 ta
• Qolgan barmoqlarda — 3 tadan

<b>Bo'g'imlari (har oyoqda):</b>
• Kaft-falanga bo'g'imlari — 5 ta
• Falangalararo bo'g'imlar — 9 ta

💡 Bitta oyoq panjasida <b>26 ta</b> suyak (7+5+14) va <b>33 ta</b> bo'g'im bor.
Ikkala oyoq panjasi — butun skelet suyaklarining <b>~1/4 qismi</b>!
""", q="foot bones"),
            ],
        ),
    ],
)
