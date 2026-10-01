from .common import category, item, section

KIDNEY = section(
    "buyrak",
    "🫘 Buyrak va siydik tizimi",
    """
<b>🫘 SIYDIK AJRATISH TIZIMI</b>

<b>Tarkibi:</b> 2 ta buyrak, 2 ta siydik yo'li, siydik pufagi, siydik chiqarish kanali.

<b>Raqamlar:</b>
• Buyraklar sutkasiga <b>~180 litr</b> qonni filtrlaydi (birlamchi siydik)
• Shundan atigi <b>1,5 litr</b> siydik bo'lib chiqadi — qolgani qayta so'riladi
• Har daqiqada buyraklardan ~1,2 litr qon o'tadi (yurak haydaydigan qonning ~20–25%)

<b>Vazifalari:</b> zaharli moddalarni chiqarish, suv-tuz muvozanati, qon bosimini boshqarish,
eritropoetin (qon hosil qilish) va D vitaminini faollashtirish.

Mavzuni tanlang 👇
""",
    [
        category(
            "anat",
            "🫘 Tuzilishi",
            "Buyrak va siydik yo'llarining tuzilishi.",
            [
                item("kidney", "Buyrak", "Ren (Nephros)", "kidney",
                     """
<b>Soni:</b> 2 ta
<b>Joylashuvi:</b> qorin bo'shlig'ining orqa devorida, umurtqa pog'onasi ikki tomonida (XII ko'krak — III bel umurtqasi). O'ng buyrak jigar sababli chapdan biroz pastda.
<b>O'lchami:</b> 10–12 sm × 5–6 sm × 3–4 sm, vazni ~150 g. Loviya shaklida.

<b>Tuzilishi:</b>
• <b>Po'stloq qavat</b> — nefronlarning koptokchalari joylashgan
• <b>Mag'iz qavat</b> — 8–12 ta buyrak piramidalari
• <b>Buyrak kosachalari → jom</b> — siydik yig'iladi
• <b>Buyrak darvozasi</b> — arteriya kiradi, vena va siydik yo'li chiqadi

Ustida <b>buyrak usti bezi</b> joylashgan.

⚠️ <b>Buzilsa:</b> buyrak yetishmovchiligi, pielonefrit, glomerulonefrit, tosh kasalligi (🩺 Kasalliklar bo'limiga qarang).
"""),
                item("nephron", "Nefron", "Nephronum", "nephron",
                     """
<b>Nefron</b> — buyrakning tuzilish va funksional birligi. Har bir buyrakda <b>~1 million</b> nefron bor.

<b>Qismlari va ishi:</b>
1. <b>Koptokcha (glomerula)</b> + Shumlyanskiy-Boumen kapsulasi — qon <u>filtrlanadi</u> → birlamchi siydik
2. <b>Proksimal kanalcha</b> — glyukoza, aminokislotalar, suv va tuzlarning ko'p qismi qayta so'riladi
3. <b>Genle qovuzlog'i</b> — siydik quyuqlashadi
4. <b>Distal kanalcha</b> — gormonlar (aldosteron) ta'sirida tuz-suv nozik boshqariladi
5. <b>Yig'uvchi naycha</b> — ADG (antidiuretik gormon) ta'sirida suv so'riladi

⚠️ <b>Buzilsa:</b> nefronlar asta-sekin nobud bo'lsa — surunkali buyrak yetishmovchiligi; koptokchalar zararlansa — siydikda oqsil va qon paydo bo'ladi.
"""),
                item("ureter", "Siydik yo'li", "Ureter", "ureter",
                     """
<b>Soni:</b> 2 ta
<b>Uzunligi:</b> 25–30 sm, diametri 3–5 mm
<b>Yo'li:</b> buyrak jomidan siydik pufagigacha

<b>Tuzilishi:</b> devorida silliq muskul bor — to'lqinsimon qisqarib (peristaltika) siydikni pufakka haydaydi.
<b>3 ta tor joyi</b> bor — toshlar ko'pincha shu joylarda tiqilib qoladi.

⚠️ <b>Buzilsa:</b> tosh tiqilsa — <i>buyrak sanchig'i</i> (juda kuchli og'riq), siydik oqimi to'xtab buyrak kengayadi (gidronefroz).
"""),
                item("bladder", "Siydik pufagi", "Vesica urinaria", "urinary bladder",
                     """
<b>Joylashuvi:</b> kichik chanoqda, qov simfizi orqasida
<b>Hajmi:</b> 350–500 ml (250–300 ml da siyish istagi paydo bo'ladi)

<b>Tuzilishi:</b>
• Devorida <b>detruzor</b> muskuli — siyganda qisqaradi
• <b>Ichki sfinkter</b> (ixtiyorsiz) va <b>tashqi sfinkter</b> (ixtiyoriy) — siydikni ushlab turadi
• Shilliq qavati burmali — cho'zilib kengayadi

⚠️ <b>Buzilsa:</b> sistit (yallig'lanish), siydik tuta olmaslik, pufak toshlari.
"""),
                item("urethra", "Siydik chiqarish kanali", "Urethra", "urethra",
                     """
<b>Vazifasi:</b> siydikni tashqariga chiqarish.

<b>Uzunligi:</b>
• Ayollarda — <b>3–5 sm</b> (kalta va keng)
• Erkaklarda — <b>18–20 sm</b> (uzun, S-simon; urug' ham shu yo'ldan o'tadi)

⚠️ <b>Buzilsa:</b> uretrit. Ayollarda kanal kalta bo'lgani uchun mikroblar pufakka oson chiqadi — sistit ayollarda ancha ko'p uchraydi.
"""),
            ],
        ),
        category(
            "dis",
            "🩺 Kasalliklar — qayer buzilsa nima bo'ladi",
            "Siydik tizimining qaysi qismi buzilganda qanday kasallik kelib chiqadi.",
            [
                item("ckd", "Buyrak yetishmovchiligi", "Insufficientia renalis", "kidney failure",
                     """
<b>📍 Qayer buziladi:</b> nefronlar — ular qonni tozalay olmay qoladi.

<b>Kelib chiqish sabablari:</b>
• <b>Qandli diabet</b> — eng ko'p sabab (yuqori qand koptokchalarni yemiradi)
• <b>Yuqori qon bosimi</b> — buyrak tomirlari zararlanadi
• Surunkali glomerulonefrit, pielonefrit
• Ba'zi dorilarni ko'p ichish (og'riq qoldiruvchilar), zaharlanish

<b>Turlari:</b>
• O'tkir — tez rivojlanadi (kuchli suvsizlanish, zaharlanish, shok), ko'pincha tuzaladi
• Surunkali — oylar-yillar davomida, qaytmas

<b>Belgilari:</b> shishlar, kam siyish, holsizlik, ko'ngil aynishi, terining qichishi, kamqonlik (eritropoetin kamayadi), qon bosimi ko'tarilishi.

<b>Davolash:</b> parhez, dori; og'ir holatda — <b>gemodializ</b> yoki buyrak ko'chirib o'tkazish.
"""),
                item("stones", "Buyrak tosh kasalligi", "Urolithiasis", "kidney stone",
                     """
<b>📍 Qayer buziladi:</b> buyrak jomi va kosachalari — siydikdagi tuzlar kristallanib tosh hosil qiladi.

<b>Kelib chiqish sabablari:</b>
• Kam suv ichish (siydik quyuqlashadi)
• Ko'p tuz, go'sht, shovul, ismaloq iste'mol qilish
• Moddalar almashinuvi buzilishi (podagra — siydik kislotasi ko'payishi)
• Issiq iqlim, kam harakat, irsiyat

<b>Tosh turlari:</b> oksalat (eng ko'p), urat, fosfat, sistin.

<b>Belgilari:</b> tosh siydik yo'liga tushsa — beldan chovga tarqaluvchi o'ta kuchli og'riq (<i>buyrak sanchig'i</i>), siydikda qon, ko'ngil aynishi.

💡 Oldini olish: kuniga 2–2,5 litr suv ichish.
"""),
                item("pyelo", "Pielonefrit", "Pyelonephritis", "pyelonephritis",
                     """
<b>📍 Qayer buziladi:</b> buyrak jomi va to'qimasi — bakterial yallig'lanish.

<b>Kelib chiqish sabablari:</b>
• Bakteriyalar (ko'pincha <i>ichak tayoqchasi</i>) siydik pufagidan yuqoriga ko'tariladi
• Siydik oqimining to'xtashi (tosh, homiladorlik, prostata kattalashishi)
• Sovqotish, immunitet pasayishi
• Davolanmagan sistit

<b>Belgilari:</b> yuqori harorat (39–40°), titrash, belda og'riq, tez-tez og'riqli siyish, loyqa siydik.

⚠️ Davolanmasa surunkaliga o'tib, buyrak yetishmovchiligiga olib kelishi mumkin.
"""),
                item("glomerulo", "Glomerulonefrit", "Glomerulonephritis", "glomerulonephritis",
                     """
<b>📍 Qayer buziladi:</b> nefron koptokchalari — immun yallig'lanish.

<b>Kelib chiqish sabablari:</b>
• Ko'pincha <b>angina yoki tomoq streptokokk infeksiyasidan 2–3 hafta keyin</b> — immun tizim xato qilib koptokchalarga hujum qiladi
• Autoimmun kasalliklar (qizil yuguruk)

<b>Belgilari (uchlik):</b>
• Shishlar — ayniqsa ertalab yuzda, ko'z atrofida
• Siydik "go'sht yuvindisi" rangida (qon aralash)
• Qon bosimi ko'tarilishi

💡 Shuning uchun anginani oxirigacha davolash muhim!
"""),
                item("cystitis", "Sistit", "Cystitis", "cystitis",
                     """
<b>📍 Qayer buziladi:</b> siydik pufagi shilliq qavati — yallig'lanish.

<b>Kelib chiqish sabablari:</b>
• Bakteriyalar siydik chiqarish kanali orqali kiradi
• Sovqotish (sovuq joyda o'tirish)
• Gigiyena buzilishi, siydikni uzoq ushlab turish

<b>Belgilari:</b> tez-tez, oz-ozdan, achishib siyish; qorinning pastida og'riq; siydikda qon bo'lishi mumkin. Odatda harorat baland bo'lmaydi.
"""),
            ],
        ),
    ],
)
