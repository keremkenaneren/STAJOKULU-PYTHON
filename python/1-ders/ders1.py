"""
a = int(input("Sayi  1 : "))
b = int(input("Sayi  2 : "))
c = int(input("Sayi  3 : "))

print("multiply : ", a*b*c)
print("sum : ", a+b+c)
print("avarage : ", (a+b+c)/3)

"""


"""
kisaKenar = int(input("kısa kenar : "))
uzunKenar = int(input("uzun kenatr : "))

print("dikdörtgenin çevresi : ", (uzunKenar+kisaKenar)*2)
print("Dikdörtgenin alanı = ", kisaKenar*uzunKenar)

"""


"""
vize1 = int(input("vize 1 : "))
vize2 = int(input("vize 2 : "))
final = int(input("final : "))

ortalama = (vize1*30/100) + (vize1*30/100) + (vize1*40/100)

print(ortalama)

"""


"""
num1 = 15
num2 = 10

if (num1 > num2):
    print("1. number")
elif (num2 > num1):
    print("2. number")
else:
    print("equals")

"""


kisaKenar = int(input("kisa kenar : "))
uzunKenar = int(input("uzun kenatr : "))

if ((kisaKenar > 0) and (uzunKenar > 0)):
    print("dikdörtgenin çevresi : ", (uzunKenar+kisaKenar)*2)
    print("Dikdörtgenin alani = ", kisaKenar*uzunKenar)
else:
    print("geçersiz değer")
