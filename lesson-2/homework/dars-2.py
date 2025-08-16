##1
ism = input("Ismigni ayt: ")
yil = int(input("tug‘ilgan yil: "))
h = 2025
if h >yil:
    print(h- yil)

##2
txt = 'LMaasleitbtui'
a =txt[::2] 
b = txt[1::2] 
print(a, b)

##3
txt = 'MsaatmiazD'
print(txt[::2], txt[-1::-2])

##4
txt1 = "I'm John. I am from London"
txt1[20::]

##5
s = input("Matn kiritng: ")
print(s[-1::-1])

##6
Matn = input("Matn kiriting ")
unli = "AEIOUaeiou"
hisob =0
for harf in Matn:
    if harf in unli:
        hisob += 1
print(hisob)

##7
sonlar = input("Sonlarni kiriting: ")
s = max(sonlar)
print(s)

##8
b = input("So'zni yozing ")

if b == b[::-1]:
    print("Bu palindrom")
else:
    print("Siz adashdiz")

##9
email= input("Email kiriting: ")
r = email.split('@')
if len(r) == 2:
    print("Domen:", r[1])
else:
    print("Notogri email")

##10
import random
import string

length= int(input("Parol uzunligini kiriting: "))
belgilar = string.ascii_letters + string.digits + string.punctuation
parol = ''.join(random.choice(belgilar) for _ in range(length))


# Misol uchun:
print(parol)
