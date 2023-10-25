# # print("""G'anisher dukondan "Python asoslari" \n degan kitob oldi!\nBu kitobda python o'rganish\nmumkin.""")
# # print("Sakkizning kvadrat ildizi", 8 * (1 / 2), "bo'ladi")
# # print("Sakson birning kvadrat ildizi", 81 ** (1 / 2), "bo'ladi")
# # print("Yigirma yettining kub ildizi", 27 ** (1 / 3))
# # print("Yigirma yettini to'rtga bo'laganda qoldiq", 27 % 4, "bo'ladi")
#
# # ism = "Sharifboy"
# # yosh = 17
# # print(ism)
# # print(yosh)
#
#
# # 1
#
# # year = int(input("Istalgan son kiriting:"))
# # kvadrat = year ** 2
# # print(45, "ning kvadrati", kvadrat, "ga teng")
# # kub = year ** 3
# # print(45, "ning kubi", kub, "ga teng")
#
# # 2
#
# # yosh = int(input("yoshingizni kiriting:"))
# # t_yosh = 2023 - yosh
# # print(f"Siz {t_yosh} da tug'ilgansiz")
#
# # 3
#
# # son_1 = int(input("Birinchi sonni kiriting:"))
# # son_2 = int(input("Ikkinchi sonni kiriting:"))
# # natija = son_1 + son_2
# # print(natija)
#
#
# # 1
# # ismlar = ["Bexruz", "Rustam", "Abror"]
# # print("Salom "+ ismlar[2],"bugun choyxona bormi?")
# # print(ismlar[1],"bugun choyxonaga boramizmi?")
#
# # 2
# # sonlar = [21, -12, 54.0,21323,-21326, -543, 34.0]
# # print(sonlar)
# #
# # sonlar[0] = sonlar[0]+sonlar[-1]
# # sonlar[1] = -76
# # sonlar[4] = sonlar[4] + 37
# # del sonlar[5]
# # print(sonlar)
#
#
# # 3
# # t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
# # z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']
# #
# # print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
# # zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
# # suhbat qilishni istar edim\n")
#
# # 4
#
# # friends = []
# # friends.append('John')
# # friends.append('Alex')
# # friends.append('Azamjon')
# # friends.append('Sobirjon')
# # friends.append('Jamshid')
# # print(friends)
# #
# # friends.remove('John')
# # friends.remove('Alex')
# # print(friends)
# #
# # friends.append('Hasan')
# # friends.insert(0, 'Husan')
# # friends.insert(2, 'Ivan')
# # friends.insert(3,"jamshid")
# # print(friends)
#
#
# # 5
#
# # mehmonlar = []
# # mehmonlar.append(friends.pop(3))
# # mehmonlar.append(friends.pop(-1))
# # mehmonlar.append(friends.pop(0))
# # print("\nKelgan mehmonlar: ", mehmonlar)
#
#
# # 1
# # davlatlar = ["amerika", "rossiya", "belgiya", "ukraina", "fransiya", "polsha"]
# # print(len(davlatlar))
# # print(sorted(davlatlar))
# # print(sorted(davlatlar, reverse=True))
# # print(davlatlar)
# # davlatlar.reverse()
# # print(davlatlar)
# # davlatlar.sort()
# # print(davlatlar)
# # print(sorted(davlatlar, reverse=True))
#
# # 2
# # sonlar = list(range(120, 1201))
# # jami = sum(sonlar)
# # ayirma = max(sonlar) - min(sonlar)
# # print(ayirma)
# # print(len(sonlar))
# # print(sonlar[:20])
# # print(sonlar[530:550])
# # print(sonlar[-20:])
#
#
# # # 3
# # taomlar = ["quymoq", "manti", "gumma", "palov", "sho'rva"]
# # nonushta = taomlar[:]
# #
# # nonushta.remove('manti')
# # nonushta.remove('gumma')
# # nonushta.remove('palov')
# # nonushta.remove("sho'rva")
# # nonushta.append('non va qaymoq')
# # nonushta.append('issiq non')
# #
# # print(taomlar)
# # print(nonushta)
#
# # nonushta = tuple(nonushta)
# # nonushta[0] = "qaymoq va non"
#
# # avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# #
# # for avto in avtolar:
# #     if avto == 'bmw':
# #         print(avto.upper())
# #     else:
# #         print(avto.title())
#
#
# # ism = input("Ismingizni nima?\n>>>")
# # if ism.lower() == "ali":
# #     print("salom, Ali")
# #
# # else:
# #     print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
#
# # yosh = int(input("yoshingiz nechida?>>>"))
# # if yosh>65: print("Siz Covid-19 risk guruhida ekansiz")
#
# # 1
# # login = input("Loginingizni kiriting: ")
# # if login.lower() == "admin":
# #     print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
# # else:
# #     print(f"Xush kelibsiz {login.title()}!")
#
# # 2
# # x = float(input("birinchi son kiriting: "))
# # y = float(input("Ikkinchi son kiriting: "))
# # if x==y: print(f"Sonlar teng:{x}={y}")
#
# # 3
# # son = int(input("Istalgan son kiriting:"))
# # print("Son manfiy") if son<0 else print("Son musbat")
#
# # 4
# # son = int(input('Istalgan son kiriting: '))
# # print(son**(1/2)) if son>0 else print('Musbat son kiriting')
#
#
# # "mehmonlar = ['Jonibek', 'Temurbek', 'Javlonbek', 'O\'tkirbek']
# # for mehmon in mehmonlar:
# #     print(f"Hurmatli {mehmon}, sizni 20-Mart kuni oshga taklif qilamiz")
# # print("Hurmat bilan, Palonchiyevlar oilasi\n")"
#
# # avtolar = ['audi','bmw','volvo','kia','hyundai']
#
#
# # for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
# #     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
# #         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
# #     else: # aks holda ...
# #         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.
#
#
# # login = input("Loginingizni kiriting: ")
# # if login == "admin":
# #     print(f"Xush kelibsiz {login.title()}")
# # else:
# #     print("kirish mumkin emas")
#
#
# # sonlar=list(range(11,100,3))
# # for son in sonlar:
# #     print(f"{son} ning kub ildizi {son**(1/3)} ga teng. ")
# # print(len(sonlar))
#
# # number = int(input("Enter the number: "))
# # if number == 10:
# #     print("number is equals to 10")
# # elif number == 50:
# #     print("number is equals to 50")
# # elif number == 100:
# #     print("number is equal to 100")
# # else:
# #     print("number is not equal to 10, 50, or 100")
#
# # from turtle import *
# # speed(1000)
# # color('cyan')
# # bgcolor('black')
# # b = 200
# # while b > 0:
# #     left(b)
# #     forward(b * 3)
# #     b = b-1
#
# # print(3 and 2 or -6//4)
#
#
# # a = 2**3**(5-3)+12//7
# # print(a)
#
# # def daraja(n):
# #     return lambda x : x**n
# #
# # kvadrat = daraja(2)
# # kub = daraja(3)
# # print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")
#
# # 1
# # mahsulotlar = ["sabzi", "yog'", "sovun", "tuxum", "piyoz", 'kartoshka', "nok", "anor", "qovun"]
# #
# # savat = []
# # for n in range(5):
# #     savat.append(input(f"Savatga {n + 1}-mahsulotni qo'shing: "))
# #
# # bor_mahsulotlar = []
# # mavjud_emas = []
# # for mahsulot in savat:
# #     if mahsulot in mahsulotlar:
# #         bor_mahsulotlar.append(mahsulot)
# #     else:
# #         mavjud_emas.append(mahsulot)
# #
# # if mavjud_emas:
# #     print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
# #     for mahsulot in mavjud_emas:
# #         print(mahsulot)
# # else:
# #     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# #
# # # 2
# # foydalanuvchilar = ["mansur", "akrom", "anvar", "sarvar", "aziz"]
# #
# # foydalanuvchi = input("Yangi login tanlang: ")
# # if foydalanuvchi in foydalanuvchilar:
# #     print("Uzr bu login band yangi login tanlang!")
# # else:
# #     print(f"Xush kelibsiz {foydalanuvchi.title()}!")
#
#
# # 1
# # taom = {
# #     'dadam': 'osh',
# #     'onam': 'manti',
# #     'opam': 'honim',
# #     'akam': 'shashlik',
# #     'men': 'lavash'
# # }
# # print(f"Dadamning sevimli taomi {taom['dadam']}.\
# # \nOnamning sevimli taomi {taom['onam']}.\
# # \nMening sevimli taomi {taom['men']}")
#
# # 2
# # python_izohli_lugati = {
# #     "integer": "Butun son",
# #     "float": "O'nlik son",
# #     "string": "Matn",
# #     "list": "Ro'yxat",
# #     "tuple": "O'zgarmas ro'yxat",
# # }
# #
# # kalit = input("Kalit so'z kiriting:").lower()
# # # print(python_izohli_lugati[kalit])
# # print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas"))
#
# # python_izohli_lugat = {
# #     "title": "Har bir so'zning bosh harfini katta harfga o'zgartiradi",
# #     "lower": "Har bir so'zni kichkina harfga o'zgartiradi",
# #     "sorted": "Har bir so'zni alifbo tartibida tahlaydi",
# #     "for": "Biror amalni qayta-qayta bajarish tsikli",
# #     "if": 'Shartlarni tekshirish operatori',
# #     "boolean": "Mantiqiy qiymat",
# #     "integer": "Butun son",
# #     "float": "O'nlik son",
# #     "numbers": 'Raqamlar',
# #     "string": "Matn",
# # }
# #
# # for kalit, qiymat in sorted(python_izohli_lugat.items()):
# #     print(f"{kalit.title()} - {qiymat}")
# #
# #
# davlatlar = {
#     "aqsh": "bishkek",
#     "italiya": "dushanbe",
#     "malaziya": "kuala-lumpur",
#     "o'zbekiston": "moskva",
#     "qirg'iziston": "nursulton",
#     "qozog'iston": "rim",
#     "rossiya": "singapur",
#     "singapur": "toshkent",
#     "tojikiston": "washington d.c."
# }
#
# print("Dunyo davlatlari:")
# for davlat in sorted(davlatlar):
#     print(davlat.upper())
#
# print("\nDavlatlarning poytaxtlari:")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())
#
# country = input("Qaysi davlatning poytaxtini bilishni istaysiz?:").lower()
# capital = davlatlar.get(country)
# if capital == None:
#     print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")


# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm,
# 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul.
# Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring)

# savol = "Yoshingizni kiriting: "
#
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#
#     if yosh < 7:
#         narh = 2000
#     elif 7 <= yosh < 18:
#         narh = 3000
#     elif 18 <= yosh < 65:
#         narh = 10000
#     else:
#         narh = 0
#
#     if narh == 0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")

# def kvadrat_kub(son):
#     """Kiritilgan sonning kvadrati va kubini konsolga chiqaruvchi funksiya"""
#     print(kvadrat_kub.__doc__)
#     print(f"{son} ning kvadrati {son ** 2} ga, kubi {son ** 3} ga teng")
#
#
# kvadrat_kub(34)
#
#
# def juft(son):
#     """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     print(juft.__doc__)
#     if son % 2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")
#
#
# juft(20)
# juft(123)

# 1.Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing
# (tub sonlar — faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)👇🏻

# def tub_sonlarni_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#
#     return tub_sonlar
#
#
# oraliq1 = int(input("Birinchi oraliq: "))
# oraliq2 = int(input("Ikkinchi oraliq: "))
# tub_oraliq = tub_sonlarni_top(oraliq1, oraliq2)
# print(tub_oraliq)

# Funkiyaga ro'yhat uzatib ro'yhatda uchragan vali ismini birinchi harfini katta harf bilan,
# qolgan elementlarini hamma harfini katta harf bilan chiqaring.Hamda ali ismli odamga salom yo'llang!

def katta_harf(ism):
    for i in range(len(ism)):
        ism[1] = ism[1].title()


ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)
