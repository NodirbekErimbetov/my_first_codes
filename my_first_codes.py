# class Avto ():
#     def __init__(self,nomi,turi,rangi):
#         self.nomi = nomi
#         self.turi = turi
#         self.rangi = rangi
#         self.yurgani = 100
#     def get_info(self):
#         return f"{self.nomi} {self.turi} {self.rangi} {self.yurgani}"
#     def update_km(self):
#         yurgani += 1
# moshina = Avto('Malibu','Avtomat','Qora')
# moshina1 = Avto('Kobalt','Mexanik','Oq')
# print(moshina.get_info())
# print((moshina1.get_info()))

# class Avto_salon():
#     def __init__(self,salon_nomi,manzil,sotuvdagi_avtolar):
#         self.salon = salon_nomi
#         self.manzil = manzil
#         self.sotuvda = sotuvdagi_avtolar
#         self.malumotlar = []
#     def add_moshina(self,moshina):
#         self.malumotlar.append(moshina)
#
# moshina = Avto_salon("Brand",'Toshkent',"Gentra,Kobalt")
# moshina.add_moshina('Gentra')
# moshina.add_moshina('Kobalt')
# print(moshina.malumotlar)
# from student import *
# class Maktab ():
#     def __init__(self,mk_nomeri,joylashgan_joyi,oquchilar_soni,mk_directori):
#         self.nomer = mk_nomeri
#         self.joyi = joylashgan_joyi
#         self.soni = oquchilar_soni
#         self.director = mk_directori
#
#     def get_info(self):
#         return f"Maktab direktori {self.director} Maktab nomeri {self.nomer} Joylashgan joyi {self.joyi} o'quvchilar soni{self.soni} "
# print("1.2 lik sanoqga")
# print("2.8 lik sanoqga")
# print("3.10 lik sanoqga")
# javob = int(input("Nechalik sanoq sistemaga o'tkazmoqchisiz:"))
# son = int(input("Son="))
# if javob ==1:
#     print("{0:0b".format(son))
# if javob ==2:
#     print("{0:07b".format(son))
# if javob ==3:
#     print("{0:0o}".format(son))

# a = int(input("a="))
# sum =  0
# while a > 0:
#     b = a%10
#     a = (a-b)/10
#     sum += b
# print("Natija:",sum)

# a = int ( input ( 'a='))
# sum = 0
# for i in range (1 ,a ):
#     if a%i == 0:
#         sum += i
#         print(f"{i}")
#     else :
#         continue
# if sum == a:
#     print("Kiritilgan son mukammal son:",a)
# else:
#     print("Kiritilgan son mukammal son emas:",a)

#
# a = int(input("a="))
# b = int(input("b="))
# if a > b:
#     for i in range(1, b + 1):
#         if a % i == 0 and b % i == 0:
#             j = i
#     print("Javob", j)
#
# if a < b:
#     for i in range(1, a + 1):
#         if a % i == 0 and b % i == 0:
#             j = i
#     print("Javob", j)

# sonlar = [100, 300, 600, 50, 35, 125]
# average_son = (max(sonlar) + min(sonlar)) // 2
# print(average_son)

# countries = ['Madrid','Spain','Portugal','Brasil','France']
# countries.sort()
# sorted(countries,reverse = False)
# countries.reverse()
# countries.sort(reverse=False)
# print(countries)

# sonlar = list(range(1 , 12,2))
# sonlar = sum(sonlar)
# print(sonlar)

# sonlar =[3, 7, 8, 12, 9, 2, 11, 45, -8]
# son = max(sonlar) - min(sonlar)
# print(son)

# sonlar = [3, 7, 8, 12, 9, 2, 11, 45, -8]
# son_ta = len(sonlar)
# print(son_ta)
#
# sonlar = list(range(1,31))
# print(sonlar[0:10])
# print(sonlar[9:20])
# print(sonlar[19:30])

# taomlar = []
# taomlar.append('osh')
# taomlar.append('somsa')
# taomlar.append('manti')
# taomlar.append('dimlama')
# taomlar.append('kabob')
# nonushta = taomlar[:]
# del nonushta[1]
# nonushta.append('choy')
# nonushta.append("sari yog'")
# print(taomlar)
#
# nonushta[0] = 'qaymoq'
# print(nonushta)

# mehmonlar = ['Ali','Vali','Bek','Hushnud','Nodir']
# for mehmon in mehmonlar:
#     print("Assalomu aleykum hush kelibsiz", mehmon)

# mehmonlar = ['Ali','Vali','Bek','Hushnud','Nodir']
# son = 0
# for mehmon in mehmonlar:
#     son = son + 1
#     print(mehmon)
# print(f"Kod {son} marta takrorlandi")

# sonlar = list(range(10 , 101 ,10))
# for son in sonlar:
#     print(f"{son} ning kubi {son**3} ga teng\n")

# p = int((input('Nechta sevimli kinoingizni bor:')))
# kinolar = []
# for n in range( 0 ,p):
#     kinolar.append((input(f"{n+1}-kinoning nomi:")))
# print(kinolar)
#
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for n in cars:
#     if n == 'gm':
#         print(n.upper())
#     else:
#         print(n.title())

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for n in cars:
#     if n != 'gm':
#         print(n.title())
#     else:
#         print(n.upper())

# n = input(("Ismingizni kiriting:"))
# if n.title() == 'Admin':
#     print("Hush kelibsiz, Admin! Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print("Hush kelibsiz!!",n.title())


# n = int(input("Istalgan son kiriting:"))
# if n > 0:
#     print("Kiritilgan son musbat")
# elif n == 0:
#     print("Nol sonini kiritdingiz")
# else:
#     print('Kiritilgan son manfiy')


# i = int ( input("Yoshingizni kiriting:"))
# if i <= 4 or 60 <= i :
#     narh = 'tekin'
# elif i <= 18 :
#     narh = 10000
# else:
#     narh = 20000
# print(f"Siz ucun kirish {narh}")

# mahsulotlar = ['osh','qazonkabob','shashlik','norin','somsa','manti','shorva','palov','qazonkabob','qovoqmanti']
# zakaz = []
# for n in range(5):
#     zakaz.append(input(f"{n+1}-zakazni kiriting :"))
# for taom in zakaz:
#     if taom in mahsulotlar:
#         print(taom, " bor")
#     else:
#         print(taom," yo'q")

# mahsulotlar = [ 'un' , 'yog\'' , 'makaron' , 'bodring' , ' pomidor' , 'olma' , 'shakar' , 'behi']
# olmoqchiman = []
# dokonda_mavjud = []
# dokonda_mavjud_emas = []
# for n in range(3):
#     olmoqchiman.append(input(f"{n+1}- mahsulotingizni kiriting :"))
# for mahsulotlarim in olmoqchiman:
#     if mahsulotlarim in mahsulotlar:
#         dokonda_mavjud.append(mahsulotlarim)
#     else:
#         dokonda_mavjud_emas.append(mahsulotlarim)
# print(dokonda_mavjud , " mahsulotlar bor")
# print(dokonda_mavjud_emas , "mahsulotlar yo'q")

# logins = [ 'Akbar' , 'Jasur' , 'Shoxa' , 'Jamshid' , 'Burxon']
# log = input("Username kiriting: ")
# if log.title() in logins :
#     print("Bu username band boshqa tanlang : ")
# else :
#     print("Hush kelibsiz : ")

# son = int(input("Son kiriting: "))
# bolinuvchilar = []
# for n in range(2, 11):
#     if son % n == 0:
#         bolinuvchilar.append(n)
# print(f"{son} soni {bolinuvchilar} ga qoldiqsiz bo'linadi")

#
# print("O'qigan kitoblaringizni kiriting agar hammasini kiritib bo'lsangiz 'stopni' kiriting :")
# while True :
#     qiymat = input()
#     if qiymat.lower() != 'stop':
#         continue
#     else:
#         print("Dastur to'xtadi!")

# yosh =("Yoshingizni kiriting(agar dasturni to'xtatmoqchi bo'lsangiz exit yoli quit ni yozing):")
#
# narh = 0
# while True:
#     qiymat = input(yosh)
#     if qiymat == 'quit' or qiymat == 'exit':
#         break
#     qiymat = int(input())
#     if int(yosh) == 7:
#         narh = 2000
#     if int(yosh) > 7 and int (yosh )<= 18:
#         narh = 3000
#     if int (yosh) > 18 and int (yosh) <= 65:
#         narh = 10000
#     if int(yosh) > 65 :
#         narh = 'bepul'
#     print("Sizga kirish ", narh)
# print("Dastur tugadi!")


# savol = "Yoshingizni kiriting:"
# while True :
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat =='quit':
#         break
#     yosh = int(qiymat)
#     if yosh == 7:
#         narh = 2000
#     if yosh > 7 and yosh <= 18:
#         narh = 3000
#     if yosh > 18 and yosh <= 65:
#         narh = 10000
#     if yosh > 65 :
#         narh = 'bepul'
#     print("Sizga kirish", narh)

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

# savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#
# while True:
#     son = input(savol)
#     # qiymat = str(savol)
#     if int(son) > 0:
#         ildiz = float(int(son) ** (0.5))
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")
#     elif qiymat.lower() == 'exit':
#         break


#
# mahsulotlar = [ ]
# ishora = True
# n = 0
# while ishora :
#     savol = input("Zakaz bermoqhi bo'lgan mahsulotlaringizni yozing: ")
#     mahsulotlar.append(savol)
#     savol1 = input(("Yana kiritasizmi (ha / yo'q) "))
#     if savol1 != 'ha' :
#         ishora = False
# for i in mahsulotlar:
#      print(f"Sizning {n+1}-zakazingiz ",i)
#      n += 1

# print("Mahsulotlar narhini kiritib chiqamiz")
# mahsulotlar = { }
# ishora = True
# n = 0
# while ishora :
#     nom = input(f"{n+1}-mahsulot nomini kiriting: ")
#     narh = input(f"{nom.title()}ning narhini kiriting:")
#     mahsulotlar[nom] = int(narh)
#     n += 1
#
#     savol = input("Yana kiritasizmi(ha/yo'q): ")
#     if savol != 'ha' :
#         ishora = False
#
# for nom , narh in mahsulotlar.items() :
#     print(f"{nom.title()}ning narhi {narh} ")

son = int(input("Necha xil meva olmoqchisiz.\n"))
#
# bor_mahsulot = ['olma', 'behi', 'qulupnay', 'uzum', 'nok', 'anor', 'erik', 'shaftoli']
#
# zakaz_ohirgi = []
# zakaz = []
# for n in range(son):
#     kirit = input(f"{n + 1}- mahsulotni kiriting: ")
#     zakaz.append(kirit)
#
# for zakaz_olingan in zakaz:
#     if zakaz_olingan in bor_mahsulot:
#         zakaz_ohirgi.append(zakaz_olingan.title())
#
# print(f"Bizda soz bergan zakazlardan quyidagilar bor \n {zakaz_ohirgi}")

# bor_mahsulot = { }
# zakaz_ohirgi = [ ]
# zakaz = [ ]
# for n in range(son) :
#     kirit = input(f"{n+1}- mahsulotni kiriting: ")
#     son = input(f"{kirit}ning narhini kiriting: ")
#     bor_mahsulot[kirit] = int(son)
# for kirit , son in bor_mahsulot.items() :
#     print(f"{kirit} ning narhi {son}")
