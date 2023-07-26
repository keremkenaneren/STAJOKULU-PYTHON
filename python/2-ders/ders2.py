"""

vize1 = int(input("vize 1 : "))
vize2 = int(input("vize 2 : "))
final = int(input("final : "))

ortalama = (vize1*30/100) + (vize1*30/100) + (vize1*40/100)

print(ortalama)

# userNote = int(input("Notunuz : "))

if ((ortalama > 90) and (ortalama <= 100)):
    print("AA")
elif (ortalama >= 80 and ortalama <= 89):
    print("BA")
elif (ortalama >= 70 and ortalama < 80):
    print("BB")
elif (ortalama >= 60 and ortalama < 70):
    print("BC")
elif (ortalama >= 50 and ortalama < 60):
    print("CC")
else:
    print("BÜTE KALDIN")


"""


"""

miktar = int(input("Ürün miktarı : "))

if (miktar >= 1 and miktar <= 10):
    print("adeti 5 TL den --", miktar * 5)
elif (miktar >= 11 and miktar <= 20):
    print("adeti 4.8 TL den --", miktar * 4.8)
elif (miktar >= 21 and miktar <= 30):
    print("adeti 4.6 TL den --", miktar * 4.6)
elif (miktar >= 31 and miktar <= 40):
    print("adeti 4.4 TL den --", miktar * 4.4)
elif (miktar >= 41 and miktar <= 50):
    print("adeti 4.2 TL den --", miktar * 4.2)
elif (miktar > 50):
    print("adeti 4 TL den --", miktar * 4)
else:
    print("Fazla miktar")


"""


"""
num1 = int(input("Büyük Sayı : "))
num2 = int(input("Küçük Sayı : "))


if (num1 % num2 == 0 and num1 != num2):
    print("katıdır")
elif (num1 == num2):
    print("eşittir")
else:
    print("değil")

"""

print("eğer üslü sayılı işlem yapacaksanız 2.sayıyı kuvvet olarak yazınız.")

num1 = int(input("1. Sayı : "))
num2 = int(input("2. Sayı : "))


islemler = int(input(
    "1-Toplama \n 2-Çıkarma \n 3-Çarpma \n 4-Bölme \n 5-Tam Saayı Bölmesi \n 6-Mod alma \n 7-Üs alma \n Yapmak İstediğiniz İşlemi seçin :"))

if (islemler == 1):
    print(num1, " + ", num2, " = ", num1 + num2)
elif (islemler == 2):
    print(num1, " - ", num2, " = ", num1 - num2)
elif (islemler == 3):
    print(num1, " * ", num2, " = ", num1 * num2)
elif (islemler == 4):
    print(num1, " / ", num2, " = ", num1 / num2)
elif (islemler == 5):
    print(num1, " // ", num2, " = ", num1 // num2)
elif (islemler == 6):
    print(num1, " % ", num2, " = ", num1 % num2)
elif (islemler == 7):
    print(num1, " ^ ", num2, " = ", num1 ** num2)
