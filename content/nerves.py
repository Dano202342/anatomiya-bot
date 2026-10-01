from .common import category, item, section

NERVES = section(
    "nerv",
    "🧠 Nerv tizimi",
    """
<b>🧠 NERV TIZIMI</b>

Nerv tizimi — organizmni boshqaruvchi va barcha a'zolar ishini muvofiqlashtiruvchi tizim.
Tanada taxminan <b>86 milliard</b> neyron (nerv hujayrasi) bor, nerv tolalarining umumiy uzunligi esa
<b>~150 000 km</b> ga yetadi.

<b>Bo'linishi:</b>
• <b>Markaziy nerv tizimi (MNT)</b> — bosh miya va orqa miya
• <b>Periferik nerv tizimi</b> — 12 juft bosh miya nervlari, 31 juft orqa miya nervlari, nerv chigallari
• <b>Vegetativ (avtonom) nerv tizimi</b> — simpatik va parasimpatik qismlar

Quyidagi bo'limlardan birini tanlang 👇
""",
    [
        category(
            "neyron",
            "🔬 Neyron va nerv tolasi",
            "Nerv tizimining eng kichik birligi — neyron. Uning tuzilishi bilan tanishing.",
            [
                item("neuron", "Neyron (nerv hujayrasi)", "Neuronum", "neuron",
                     """
<b>Tuzilishi:</b>
• <b>Tana (soma)</b> — yadro joylashgan qism
• <b>Dendritlar</b> — signalni <u>qabul qiluvchi</u> kalta, shoxlangan o'simtalar
• <b>Akson</b> — signalni <u>uzatuvchi</u> bitta uzun o'simta (1 metrgacha bo'lishi mumkin!)
• <b>Akson uchlari (terminallar)</b> — keyingi hujayraga signal beradi

<b>Turlari (vazifasiga ko'ra):</b>
• Sezuvchi (afferent) — retseptordan MNTga
• Harakatlantiruvchi (efferent) — MNTdan muskulga
• Oraliq (interneyron) — neyronlarni bog'laydi

💡 Eng uzun neyron — oyoqdagi quymich nervi tolalari, orqa miyadan oyoq barmog'igacha boradi.
""", q="neuron 3D"),
                item("myelin", "Miyelin qobiq va nerv tolasi", "Vagina myelini", "myelin sheath",
                     """
<b>Nerv tolasi</b> — qobiq bilan o'ralgan akson.

• <b>Miyelin qobiq</b> — aksonni o'rab turuvchi yog'li "izolyatsiya". MNTda <i>oligodendrotsitlar</i>,
  periferiyada <i>Shvann hujayralari</i> hosil qiladi.
• <b>Ranv'e bo'g'iqlari</b> — qobiqdagi oraliqlar; impuls ulardan "sakrab" o'tadi.

<b>Tezlik:</b>
• Miyelinli tola — <b>120 m/s</b> gacha (≈430 km/soat)
• Miyelinsiz tola — 0,5–2 m/s

<b>Nerv tuzilishi:</b> tolalar endonevriy bilan, tola dastalari perinevriy bilan, butun nerv epinevriy bilan o'ralgan.

⚠️ Miyelin buzilishi — <i>tarqoq skleroz</i> kasalligining asosi.
"""),
                item("synapse", "Sinaps", "Synapsis", "synapse",
                     """
<b>Sinaps</b> — ikki neyron (yoki neyron va muskul) o'rtasidagi aloqa joyi.

<b>Tuzilishi:</b>
• Presinaptik membrana — mediator pufakchalari bor
• Sinaptik yoriq — ~20 nm kenglikdagi bo'shliq
• Postsinaptik membrana — retseptorlar joylashgan

<b>Asosiy mediatorlar:</b> atsetilxolin, noradrenalin, dofamin, serotonin, GAMK, glutamat.

💡 Bitta neyron 10 000 tagacha sinaps hosil qilishi mumkin.
"""),
            ],
        ),
        category(
            "mnt",
            "🧠 Markaziy nerv tizimi",
            "Bosh miya va orqa miya — nerv tizimining \"boshqaruv markazi\".",
            [
                item("cerebrum", "Katta yarim sharlar (bosh miya)", "Cerebrum", "cerebrum",
                     """
<b>Joylashuvi:</b> kalla qutisi ichida. Bosh miya vazni ~1300–1400 g.

<b>4 ta asosiy bo'lagi:</b>
• <b>Peshona bo'lagi</b> — fikrlash, rejalash, ixtiyoriy harakat, nutq (Broka markazi)
• <b>Tepa bo'lagi</b> — teri sezgisi, fazoda mo'ljal olish
• <b>Chakka bo'lagi</b> — eshitish, xotira, nutqni tushunish (Vernike markazi)
• <b>Ensa bo'lagi</b> — ko'rish

<b>Qobiq (kulrang modda)</b> qalinligi 2–4 mm, unda ~16 mlrd neyron.
Ikki yarim shar <b>qadoqsimon tana</b> (corpus callosum) orqali bog'langan.
""", q="cerebrum"),
                item("cerebellum", "Miyacha", "Cerebellum", "cerebellum",
                     """
<b>Joylashuvi:</b> ensa bo'lagining ostida, kalla orqa chuqurchasida.

<b>Vazifasi:</b>
• Harakatlarni muvofiqlashtirish (koordinatsiya)
• Muvozanat va tana holatini saqlash
• Harakatni o'rganish (velosiped haydash va h.k.)

💡 Miyacha bosh miya hajmining ~10% ini tashkil etadi, lekin barcha neyronlarning <b>yarmidan ko'pi</b> shu yerda!
"""),
                item("brainstem", "Miya ustuni", "Truncus encephali", "brainstem",
                     """
<b>Tarkibi:</b> o'rta miya, Varoliy ko'prigi, uzunchoq miya.

<b>Vazifasi:</b>
• Nafas olish va yurak urishini boshqarish
• Yutish, yo'tal, aksirish reflekslari
• 12 juft bosh miya nervining <b>10 tasi (III–XII)</b> yadrolari shu yerda

⚠️ Hayot uchun eng muhim markazlar shu yerda joylashgan.
"""),
                item("spinalcord", "Orqa miya", "Medulla spinalis", "spinal cord",
                     """
<b>Joylashuvi:</b> umurtqa kanali ichida, I bo'yin umurtqasidan I–II bel umurtqasigacha.
<b>Uzunligi:</b> 42–45 sm, qalinligi ~1 sm.

<b>Tuzilishi:</b>
• Markazda — "kapalak" shaklidagi <b>kulrang modda</b> (neyron tanalari)
• Atrofida — <b>oq modda</b> (o'tkazuvchi yo'llar)
• Pastki uchi — <i>ot dumi</i> (cauda equina) nervlari

<b>Segmentlar:</b> 31 ta (8 bo'yin, 12 ko'krak, 5 bel, 5 dumg'aza, 1 dum) — har biridan 1 juft nerv chiqadi.

<b>Vazifasi:</b> reflekslar (masalan, tizza refleksi) va miya bilan tana orasida signal o'tkazish.
"""),
            ],
        ),
        category(
            "kranial",
            "👁 12 juft bosh miya nervlari",
            """
Bosh miyadan to'g'ridan-to'g'ri chiqadigan <b>12 juft</b> nerv. Rim raqamlari bilan belgilanadi.
Eslab qolish uchun: <i>sezuvchi</i> (S), <i>harakat</i> (H), <i>aralash</i> (A).
""",
            [
                item("cn1", "I. Hid bilish nervi", "N. olfactorius", "olfactory nerve",
                     """
<b>Turi:</b> sezuvchi (S)
<b>Boshlanishi:</b> burun bo'shlig'i shilliq qavatidagi hid retseptorlari
<b>Yo'li:</b> g'alvirsimon suyak teshikchalari orqali hid bilish piyozchasiga

<b>Vazifasi:</b> hidlarni sezish

⚠️ Zararlanganda — <i>anosmiya</i> (hid sezmaslik).
"""),
                item("cn2", "II. Ko'rish nervi", "N. opticus", "optic nerve",
                     """
<b>Turi:</b> sezuvchi (S)
<b>Boshlanishi:</b> ko'z to'r pardasi (retina) ganglioz hujayralari
<b>Yo'li:</b> ko'z kosasi → ko'rish kanali → <b>ko'rish kesishmasi (chiasma)</b> → ensa bo'lagi

<b>Vazifasi:</b> ko'rish
<b>Uzunligi:</b> ~4,5–5 sm, ~1,2 mln tola

💡 Chiasmada har bir ko'zning ichki (burun tomondagi) tolalari qarama-qarshi tomonga o'tadi.
"""),
                item("cn3", "III. Ko'zni harakatlantiruvchi nerv", "N. oculomotorius", "oculomotor nerve",
                     """
<b>Turi:</b> harakatlantiruvchi (H) + parasimpatik
<b>Boshlanishi:</b> o'rta miya

<b>Innervatsiya qiladi:</b>
• Ko'zning yuqori, pastki, ichki to'g'ri muskullari
• Pastki qiyshiq muskul
• Yuqori qovoqni ko'taruvchi muskul
• Ko'z qorachig'ini toraytiruvchi va kiprikli muskul (parasimpatik)

⚠️ Zararlanganda — qovoq tushishi (ptoz), ko'z tashqariga-pastga qaraydi, qorachiq kengayadi.
"""),
                item("cn4", "IV. G'altak nervi", "N. trochlearis", "trochlear nerve",
                     """
<b>Turi:</b> harakatlantiruvchi (H)
<b>Boshlanishi:</b> o'rta miya (miya ustunining <u>orqa</u> yuzasidan chiqadigan yagona nerv)

<b>Innervatsiya qiladi:</b> ko'zning <b>yuqori qiyshiq muskuli</b> — ko'zni pastga va tashqariga buradi.

💡 Bosh miya nervlarining eng ingichkasi va kalla ichidagi yo'li eng uzuni.
"""),
                item("cn5", "V. Uch shoxli nerv", "N. trigeminus", "trigeminal nerve",
                     """
<b>Turi:</b> aralash (A) — eng yo'g'on bosh miya nervi
<b>Boshlanishi:</b> Varoliy ko'prigi

<b>3 ta shoxi:</b>
• <b>V1 — Ko'z nervi</b> (n. ophthalmicus): peshona, yuqori qovoq, burun terisi, shox parda
• <b>V2 — Yuqori jag' nervi</b> (n. maxillaris): yonoq, yuqori lab, yuqori tishlar
• <b>V3 — Pastki jag' nervi</b> (n. mandibularis): pastki lab, iyak, pastki tishlar + <b>chaynov muskullari</b>

<b>Vazifasi:</b> yuz sezgisi va chaynash.
⚠️ Kasalligi — <i>trigeminal nevralgiya</i> (kuchli yuz og'rig'i).
"""),
                item("cn6", "VI. Uzoqlashtiruvchi nerv", "N. abducens", "abducens nerve",
                     """
<b>Turi:</b> harakatlantiruvchi (H)
<b>Boshlanishi:</b> Varoliy ko'prigi

<b>Innervatsiya qiladi:</b> ko'zning <b>tashqi (lateral) to'g'ri muskuli</b> — ko'zni tashqariga buradi.

⚠️ Zararlanganda — ichkariga g'ilaylik, ikkita ko'rish (diplopiya).
"""),
                item("cn7", "VII. Yuz nervi", "N. facialis", "facial nerve",
                     """
<b>Turi:</b> aralash (A)
<b>Boshlanishi:</b> Varoliy ko'prigi → ichki eshitish yo'li → yuz kanali → bigizsimon-so'rg'ichsimon teshik → quloq oldi bezi ichida 5 shoxga bo'linadi

<b>5 shoxi:</b> chakka, yonoq, lunj, pastki jag' chekka, bo'yin shoxlari

<b>Vazifasi:</b>
• Barcha <b>mimika muskullari</b> (kulish, qosh chimirish)
• Tilning oldingi 2/3 qismida ta'm sezish
• Ko'z yosh, jag' osti va til osti so'lak bezlari

⚠️ Zararlanganda — <i>Bell falaji</i> (yuzning bir tomoni "osilib" qoladi).
"""),
                item("cn8", "VIII. Dahliz-chig'anoq nervi", "N. vestibulocochlearis", "vestibulocochlear nerve",
                     """
<b>Turi:</b> sezuvchi (S)
<b>Boshlanishi:</b> ichki quloq

<b>2 qismi:</b>
• <b>Chig'anoq (eshitish) qismi</b> — tovushni eshitish
• <b>Dahliz (vestibulyar) qismi</b> — muvozanat, bosh holatini sezish

⚠️ Zararlanganda — karlik, quloq shang'illashi, bosh aylanishi.
"""),
                item("cn9", "IX. Til-halqum nervi", "N. glossopharyngeus", "glossopharyngeal nerve",
                     """
<b>Turi:</b> aralash (A)
<b>Boshlanishi:</b> uzunchoq miya, bo'yinturuq teshigi orqali chiqadi

<b>Vazifasi:</b>
• Tilning orqa 1/3 qismida ta'm va sezgi
• Halqum sezgisi (qusish refleksi)
• Quloq oldi so'lak bezi
• Uyqu arteriyasi sinusidan qon bosimi haqida ma'lumot
"""),
                item("cn10", "X. Adashgan nerv", "N. vagus", "vagus nerve",
                     """
<b>Turi:</b> aralash (A) — eng uzun va eng keng tarqalgan bosh miya nervi
<b>Boshlanishi:</b> uzunchoq miya → bo'yin → ko'krak → qorin bo'shlig'i

<b>Innervatsiya qiladi:</b>
• Halqum va hiqildoq muskullari (ovoz, yutish)
• <b>Yurak</b> — urishni sekinlashtiradi
• O'pka, bronxlar
• Qizilo'ngach, oshqozon, ichaklar (yo'g'on ichakning chap egilishigacha)

💡 "Vagus" — lotincha "adashib yuruvchi", chunki tananing ko'p joyiga tarqaladi.
Parasimpatik tizimning asosiy nervi.
"""),
                item("cn11", "XI. Qo'shimcha nerv", "N. accessorius", "accessory nerve",
                     """
<b>Turi:</b> harakatlantiruvchi (H)
<b>Boshlanishi:</b> uzunchoq miya va orqa miyaning yuqori bo'yin segmentlari

<b>Innervatsiya qiladi:</b>
• <b>To'sh-o'mrov-so'rg'ichsimon muskul</b> — boshni burish
• <b>Trapetsiyasimon muskul</b> — yelkani ko'tarish

⚠️ Zararlanganda — yelka tushadi, boshni burish qiyinlashadi.
"""),
                item("cn12", "XII. Til osti nervi", "N. hypoglossus", "hypoglossal nerve",
                     """
<b>Turi:</b> harakatlantiruvchi (H)
<b>Boshlanishi:</b> uzunchoq miya, til osti kanali orqali chiqadi

<b>Innervatsiya qiladi:</b> tilning deyarli barcha muskullari.
<b>Vazifasi:</b> gapirish, chaynash, yutishda til harakati.

⚠️ Zararlanganda — til chiqarilganda shikastlangan tomonga og'adi.
"""),
            ],
        ),
        category(
            "spinal",
            "🦴 Orqa miya nervlari va chigallar",
            """
Orqa miyadan <b>31 juft</b> nerv chiqadi:
• 8 juft bo'yin (C1–C8)
• 12 juft ko'krak (T1–T12)
• 5 juft bel (L1–L5)
• 5 juft dumg'aza (S1–S5)
• 1 juft dum (Co1)

Ular birlashib <b>nerv chigallari</b> (pleksuslar) hosil qiladi.
""",
            [
                item("cervplex", "Bo'yin chigali", "Plexus cervicalis", "cervical plexus",
                     """
<b>Hosil bo'lishi:</b> C1–C4 nervlari
<b>Joylashuvi:</b> bo'yinning yon tomonida, to'sh-o'mrov-so'rg'ichsimon muskul ostida

<b>Asosiy shoxlari:</b>
• Kichik ensa nervi, katta quloq nervi — teri sezgisi
• Bo'yinning ko'ndalang nervi, o'mrov usti nervlari
• <b>Diafragma nervi</b> (n. phrenicus, C3–C5) — eng muhimi!

💡 "C3, 4, 5 — diafragmani tirik tutadi" — tibbiyot talabalari iborasi.
"""),
                item("phrenic", "Diafragma nervi", "N. phrenicus", "phrenic nerve",
                     """
<b>Hosil bo'lishi:</b> C3–C5
<b>Yo'li:</b> oldingi narvonsimon muskul ustidan pastga → ko'krak qafasi → yurak oldidan → diafragma

<b>Vazifasi:</b> <b>diafragmani</b> harakatlantiradi — asosiy nafas muskuli!

⚠️ Ikkala tomondan shikastlanishi o'z-o'zidan nafas olishni to'xtatadi.
💡 Hiqichoq — diafragmaning ixtiyorsiz qisqarishi.
"""),
                item("brachplex", "Yelka chigali", "Plexus brachialis", "brachial plexus",
                     """
<b>Hosil bo'lishi:</b> C5–C8 va T1 nervlari
<b>Joylashuvi:</b> bo'yindan o'mrov ostidan qo'ltiq ostiga

<b>Tuzilishi:</b> ildizlar → 3 ta stvol → bo'linmalar → 3 ta tutam → shoxlar

<b>5 ta asosiy shoxi:</b>
• Mushak-teri nervi
• Qo'ltiq nervi
• Bilak nervi (radialis)
• O'rta nerv (medianus)
• Tirsak nervi (ulnaris)

<b>Vazifasi:</b> butun qo'lni harakatlantiradi va sezgi beradi.
"""),
                item("intercost", "Qovurg'alararo nervlar", "Nn. intercostales", "intercostal nerves",
                     """
<b>Hosil bo'lishi:</b> T1–T11 (T12 — qovurg'a ostidagi nerv)
<b>Joylashuvi:</b> har bir qovurg'aning pastki qirrasi bo'ylab, arteriya va vena bilan birga

<b>Vazifasi:</b>
• Qovurg'alararo muskullar (nafas olish)
• Qorin devori muskullari
• Ko'krak va qorin terisi sezgisi

💡 Bu nervlar chigal hosil qilmaydi — segment-segment joylashadi.
"""),
                item("lumbplex", "Bel chigali", "Plexus lumbalis", "lumbar plexus",
                     """
<b>Hosil bo'lishi:</b> L1–L4 (qisman T12)
<b>Joylashuvi:</b> katta bel muskuli ichida

<b>Asosiy shoxlari:</b>
• Yonbosh-qorin osti, yonbosh-chov nervlari
• Son-jinsiy nerv
• Sonning tashqi teri nervi
• <b>Son nervi</b> (n. femoralis)
• <b>Yopqich nerv</b> (n. obturatorius)
"""),
                item("sacrplex", "Dumg'aza chigali", "Plexus sacralis", "sacral plexus",
                     """
<b>Hosil bo'lishi:</b> L4–S4
<b>Joylashuvi:</b> kichik chanoq orqa devorida, noksimon muskul ustida

<b>Asosiy shoxlari:</b>
• Yuqori va pastki dumba nervlari — dumba muskullari
• <b>Quymich nervi</b> — tanadagi eng yo'g'on nerv
• Uyat nervi (n. pudendus)
• Sonning orqa teri nervi
"""),
            ],
        ),
        category(
            "arm",
            "💪 Qo'l nervlari",
            "Yelka chigalidan chiqadigan qo'lning asosiy nervlari.",
            [
                item("axillary", "Qo'ltiq nervi", "N. axillaris", "axillary nerve",
                     """
<b>Hosil bo'lishi:</b> C5–C6 (orqa tutam)
<b>Yo'li:</b> yelka suyagining jarrohlik bo'yni atrofidan aylanib o'tadi

<b>Innervatsiya qiladi:</b>
• <b>Deltasimon muskul</b> — qo'lni yon tomonga ko'tarish
• Kichik yumaloq muskul
• Yelka ustki-tashqi terisi

⚠️ Yelka chiqishi yoki suyak sinishida shikastlanishi mumkin.
"""),
                item("musculocut", "Mushak-teri nervi", "N. musculocutaneus", "musculocutaneous nerve",
                     """
<b>Hosil bo'lishi:</b> C5–C7 (lateral tutam)
<b>Yo'li:</b> tumshuqsimon-yelka muskulini teshib o'tadi

<b>Innervatsiya qiladi:</b>
• <b>Ikki boshli muskul</b> (biceps), yelka muskuli, tumshuqsimon-yelka muskuli — tirsakni bukish
• Bilakning tashqi terisi
"""),
                item("radial", "Bilak nervi", "N. radialis", "radial nerve",
                     """
<b>Hosil bo'lishi:</b> C5–T1 (orqa tutam) — yelka chigalining eng yirik shoxi
<b>Yo'li:</b> yelka suyagi orqasidagi spiral egat bo'ylab aylanadi

<b>Innervatsiya qiladi:</b>
• <b>Uch boshli muskul</b> (triceps) — tirsakni yozish
• Bilak va barmoqlarni yozuvchi barcha muskullar
• Qo'lning orqa yuzasi terisi

⚠️ Shikastlanganda — <i>"osilgan panja"</i>: kaftni ko'tara olmaslik.
"""),
                item("median", "O'rta nerv", "N. medianus", "median nerve",
                     """
<b>Hosil bo'lishi:</b> C6–T1 (lateral va medial tutamlar)
<b>Yo'li:</b> yelka o'rtasidan → tirsak chuqurchasi → bilak o'rtasi → <b>kaft usti kanali</b>

<b>Innervatsiya qiladi:</b>
• Bilakni bukuvchi muskullarning ko'pchiligi
• Bosh barmoq tepaligi muskullari
• Kaftning bosh, ko'rsatkich, o'rta va nomsiz barmoqning yarmi terisi

⚠️ <i>Karpal tunnel sindromi</i> — kanalda siqilishi (kompyuterda ko'p ishlaganda).
Shikastlanganda — <i>"voiz qo'li"</i>.
"""),
                item("ulnar", "Tirsak nervi", "N. ulnaris", "ulnar nerve",
                     """
<b>Hosil bo'lishi:</b> C8–T1 (medial tutam)
<b>Yo'li:</b> tirsakda yelka suyagining ichki do'ngchasi orqasidan o'tadi

<b>Innervatsiya qiladi:</b>
• Kaftning mayda muskullari (barmoqlarni yoyish-yig'ish)
• Jimjiloq tepaligi
• Jimjiloq va nomsiz barmoqning yarmi terisi

💡 Tirsakni urganda "tok urgandek" his — aynan shu nerv!
⚠️ Shikastlanganda — <i>"panjasimon qo'l"</i>.
"""),
            ],
        ),
        category(
            "leg",
            "🦵 Oyoq nervlari",
            "Bel va dumg'aza chigallaridan chiqadigan oyoqning asosiy nervlari.",
            [
                item("femoral", "Son nervi", "N. femoralis", "femoral nerve",
                     """
<b>Hosil bo'lishi:</b> L2–L4 (bel chigali)
<b>Yo'li:</b> chov boylami ostidan songa chiqadi

<b>Innervatsiya qiladi:</b>
• <b>To'rt boshli muskul</b> — tizzani yozish
• Tikuvchi muskul, yonbosh-bel muskuli
• Sonning old yuzasi va boldirning ichki terisi (teri osti nervi orqali)

⚠️ Shikastlanganda — tizza refleksi yo'qoladi, zinadan chiqish qiyinlashadi.
"""),
                item("obturator", "Yopqich nerv", "N. obturatorius", "obturator nerve",
                     """
<b>Hosil bo'lishi:</b> L2–L4 (bel chigali)
<b>Yo'li:</b> chanoq suyagidagi yopqich teshik orqali sonning ichki tomoniga

<b>Innervatsiya qiladi:</b>
• Sonni yaqinlashtiruvchi (adduktor) muskullar — oyoqlarni jipslashtirish
• Sonning ichki terisi
"""),
                item("sciatic", "Quymich nervi", "N. ischiadicus", "sciatic nerve",
                     """
<b>Hosil bo'lishi:</b> L4–S3 (dumg'aza chigali)
<b>Yo'li:</b> katta quymich teshigi → dumba ostida → sonning orqa tomoni → tizza osti chuqurchasida 2 ga bo'linadi

<b>Xususiyati:</b> tanadagi <b>eng yo'g'on va eng uzun nerv</b> (yo'g'onligi barmoqdek ~1–2 sm).

<b>Innervatsiya qiladi:</b>
• Sonning orqa muskullari (tizzani bukish)
• Tizzadan pastdagi deyarli barcha muskul va teri (shoxlari orqali)

<b>Shoxlari:</b> katta boldir nervi, umumiy kichik boldir nervi.
⚠️ <i>Ishias</i> — nervning siqilishi, oyoqqa tarqaluvchi og'riq.
"""),
                item("tibial", "Katta boldir nervi", "N. tibialis", "tibial nerve",
                     """
<b>Hosil bo'lishi:</b> quymich nervining shoxi (L4–S3)
<b>Yo'li:</b> tizza osti chuqurchasi → boldir orqasi → ichki to'piq orqasidan tovonga

<b>Innervatsiya qiladi:</b>
• Boldir orqa muskullari (<b>boldir muskuli</b>, kambalasimon) — oyoq uchida turish
• Barmoqlarni bukuvchi muskullar
• Oyoq tagi terisi va muskullari
"""),
                item("fibular", "Umumiy kichik boldir nervi", "N. fibularis (peroneus) communis", "common fibular nerve",
                     """
<b>Hosil bo'lishi:</b> quymich nervining shoxi (L4–S2)
<b>Yo'li:</b> kichik boldir suyagi boshchasi atrofidan aylanib o'tadi (teri ostida, juda yuza!)

<b>Shoxlari:</b>
• Yuza shoxi — kichik boldir muskullari (oyoqni tashqariga burish)
• Chuqur shoxi — oyoq panjasini va barmoqlarni yuqoriga ko'taruvchi muskullar

⚠️ Shikastlanganda — <i>"osilgan oyoq"</i>: yurganda panja yerga sudraladi ("xo'roz yurishi").
Oyoq ustiga oyoq qo'yib uzoq o'tirganda siqilishi mumkin.
"""),
                item("gluteal", "Dumba nervlari", "Nn. glutei superior et inferior", "gluteal nerves",
                     """
<b>Yuqori dumba nervi</b> (L4–S1):
• O'rta va kichik dumba muskullari — yurganda chanoqni ushlab turadi

<b>Pastki dumba nervi</b> (L5–S2):
• <b>Katta dumba muskuli</b> — o'tirgan joydan turish, zinaga chiqish

⚠️ Dumbaga ukol noto'g'ri qilinsa shikastlanishi mumkin — shuning uchun ukol <b>yuqori-tashqi chorakka</b> qilinadi.
""", q="gluteal nerve"),
                item("pudendal", "Uyat nervi", "N. pudendus", "pudendal nerve",
                     """
<b>Hosil bo'lishi:</b> S2–S4 (dumg'aza chigali)
<b>Yo'li:</b> chanoqdan chiqib, yana kichik quymich teshigi orqali oraliqqa qaytadi

<b>Innervatsiya qiladi:</b>
• Oraliq muskullari
• Siydik va to'g'ri ichakning tashqi sfinkterlari (ixtiyoriy nazorat)
• Tashqi jinsiy a'zolar terisi
"""),
            ],
        ),
        category(
            "ans",
            "⚡️ Vegetativ nerv tizimi",
            "Ichki a'zolarni <b>ixtiyorsiz</b> boshqaradigan tizim: yurak, ichak, bezlar, qon tomirlar.",
            [
                item("sympathetic", "Simpatik nerv tizimi", "Pars sympathica", "sympathetic nervous system",
                     """
<b>Joylashuvi:</b> orqa miyaning T1–L2 segmentlari + umurtqa pog'onasi yonidagi <b>simpatik stvol</b> (zanjir shaklidagi tugunlar)

<b>"Jang yoki qoch" reaksiyasi:</b>
• Yurak urishi tezlashadi, bosim ko'tariladi
• Qorachiq kengayadi
• Bronxlar kengayadi
• Hazm qilish sekinlashadi
• Ter ajralishi kuchayadi
• Buyrak usti bezidan adrenalin ajraladi

<b>Asosiy mediator:</b> noradrenalin
""", q="sympathetic trunk"),
                item("parasympathetic", "Parasimpatik nerv tizimi", "Pars parasympathica", "parasympathetic nervous system",
                     """
<b>Joylashuvi:</b> miya ustuni (III, VII, IX, X bosh miya nervlari) + orqa miyaning S2–S4 segmentlari

<b>"Dam olish va hazm qilish" reaksiyasi:</b>
• Yurak urishi sekinlashadi
• Qorachiq torayadi
• So'lak ajralishi, ichak harakati kuchayadi
• Siydik pufagi qisqaradi

<b>Asosiy nervi:</b> adashgan nerv (vagus) — parasimpatik tolalarning ~75% i
<b>Asosiy mediator:</b> atsetilxolin
""", q="vagus nerve"),
            ],
        ),
    ],
)
