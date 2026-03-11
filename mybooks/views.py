from django.shortcuts import render
from django.http import HttpResponse
# bu malumotni ai dan oldin chunki buncha tuliq malumot bilmayman lekin qanday berishni uzim aytdim
#  unga menga uzbdagi mashhur kitoblar haqida malumot kerak
#  menga ularni id ga dict tenglab yani id sini aytsa malumotlari keladigan va ushlardan dict bulgani uchun foydalanaman dedim
BOOKS_DATA = {
    1: {
        "name": "O'tkan kunlar",
        "author": "Abdulla Qodiriy",
        "date": "1922-01-01",
        "desc": "O'zbek romanchiligining asosi bo'lgan asar. Otabek va Kumushning fojiaviy sevgisi."
    },
    2: {
        "name": "Dunyoning ishlari",
        "author": "O'tkir Hoshimov",
        "date": "1982-01-01",
        "desc": "Ona mehri va insoniy qadriyatlar haqidagi ta'sirli hikoyalar to'plami."
    },
    3: {
        "name": "Yulduzli tunlar",
        "author": "Pirimqul Qodirov",
        "date": "1978-01-01",
        "desc": "Zahiriddin Muhammad Bobur hayoti va uning murakkab taqdiri haqida tarixiy roman."
    },
    4: {
        "name": "Sariq devni minib",
        "author": "Xudoyberdi To'xtaboyev",
        "date": "1968-01-01",
        "desc": "Hoshimjonning sarguzashtlari orqali bolalar dunyosini ochib beruvchi ajoyib asar."
    }
}
# Create your views here.


# ustoz rostini aytaman men html juda yaxsh bilaman lekin css ni ham bilaman ozroq class ochib uni shunga ulab quysa usha css kodida edit bulishini , lekin bazi jot\ylarini ai dan yordam suradim
# masalan color va font-size ni ai dan oldim , css ni ham ai qilib berdi chunki uzi backend dasturchiman frontedni ham ozroq bilan kuproq html lekin javascript va css ni hover marginlarni emas

def shelf(request):
    html = """
    <style>
        .book-item {
            margin-bottom: 20px;
            padding: 10px;
            border-bottom: 1px solid #eee;
        }
        .book-link {
            font-size: 20px;
            font-weight: bold;
            text-decoration: none;
            color: #2c3e50;
        }
        .book-link:hover { color: #3498db; }
    </style>
    <h1>Mening kitob javonim</h1>
    <hr>
    """

    # hamma bizda bor kitoblarni ustma ust quyish uchun for loop ishlatdim chunki uni tugashi aniq shu uchun while shart emas
    # shelf funksiyasi ichida:
    for b_id, b_info in BOOKS_DATA.items():
        html += f"""
        <div class="book-item">
            <a href="/books/{b_id}/" class="book-link">{b_info['name']}</a>
            <p>Muallif: {b_info['author']}</p>
        </div>
        """

    return HttpResponse(html)

# bu yeri juda oddiy va osson agar usha url dagi id books_data da bulsa uni b ga tenglaydi yani usha id si key value uni malumotlari b uni itemsga teng buladi
# div ham osson <hr> tegi juda osson, malumot olish bundan ham oson usha b deymizda tortburchak qovusda nima kerakligi yozamiz bu juda osson dict ni ishlatish
def book(request, book_id):
    if book_id in BOOKS_DATA:
        b = BOOKS_DATA[book_id]
        html = f"""
        <div style="font-family: sans-serif; max-width: 600px; margin: 20px auto;">

            <a href="/books/">← Orqaga qaytish</a>
            <h1 style="color: #2c3e50;">{b['name']}</h1>
            <p><b>ID raqami:</b> {book_id}</p>
            <p><b>Muallif:</b> {b['author']}</p>
            <p><b>Nashr yili:</b> {b['date']}</p>
            <hr>
            <p style="line-height: 1.6;"><b>Tavsif:</b> {b['desc']}</p>
        </div>
        """
    else:
        #  agar uha id li masalan 99999 id li yoki umuman a2as bulsa shu chiqadi chunki bizda 1,2,3,4 id lar bor boshqa id hali  yoq, qushsam bulardi ai bilan lekin qushmadim
        html = "<h1>Xato: Kitob topilmadi!</h1><a href='/books/'>← Orqaga qaytish</a>"

    return HttpResponse(html)
# !!!!ILTIMOS!!! pastdagilarni yaxshilab uqing va tushuning
# agar ustoz aytdanda database ga ulab ham qilardim 43 darsdagi uyga vazifani qilganimday,
# databse class ochib methodlarni yozib shunaqa unda bundan ham osson va qiziqarli bulasdi lekin vaqtim bulmadi boshqa kursga ham boramanda
#  ustoz lekin ai dan foydalanganim uzimga ham yoqmaydi lekin men frontend,backend, databse ni tuliq yoki yaxshi bilmaymanda shunga sizdan surayman?
#  AI dan foydalansam uzim ham kodni uzim yozmagan bulaman bir xil payt mni algoritm yechimimdan ham yaxshroq yechim beradida va menikidan ham optmal yechim bulsa unikini tushunib olaman qayerda,qayerga ishlatishni bilib usha yerga CTRL + V qilaman,
#  va uim dan kunglim tolmaydi men uzim emas ai qilganday bulyabman deb, Sababi u PYthon boshqa barcha tillarni tuliq biladi yani men bilgan algoritm va koddan ham oson uslu python kutubxonalarini tavsiya qilad
#  MEn ham pytho tuliq urgansam ushanday eng optiaml ishlatasdim lekin hozircha yuq ,hozircha uzim bilgan bilimga tayanib qilaman va bir xil payt ai niki menikidan 1000 baravar tez osson va qisqa kod buladi
#  Bilmagan joylarimni , narsalar , bug , applarni Gemini,Chatgpt lardan surab qilaymi yoki tuliq 0 dan yuriq nomasiz uzim qilaymi vaqt olsa ham , Telegramda yozing uzim ga guruhda hamma kurishini hohlamayman Ha yoki Yoq deb yozing
#  Telegram akkountim Firdavs Yo'ldoshev @firdavsy2011
