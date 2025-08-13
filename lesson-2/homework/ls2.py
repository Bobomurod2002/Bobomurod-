txt = 'MsaatmiazD'
txt[::2]

txt[-1::-2]


txt1 = "I'm John. I am from London"
txt1[20::]


txt2 = "London is the capital of England"
txt2[::-1]


b = input("So'zni yozing ")
if b == b[::-1]:
    print("Bu palindrom")
else:
    print("Siz adashdiz")


meva = ['olma', 'banan','anor', 'uzum', 'shaftoli']
print(meva[2])


a = [1,3,5,7,9]
b = [2,4,6,8,10]
a.extend(b)
print(a)


r = [10,15,20,25,30,35]
boshi =r[0]
boshi

ortasi = len(r) //2
orta = r[3]
orta

oxiri = r[-1]
oxiri


b =[boshi, orta, oxiri]
print(b)


shaharlar =['Madrid', 'London', 'Berlin', ]
if "Paris" in shaharlar:
    print("Great")
else:
    print("Not found")


a = [5,7,9,11,13,15]
b =a *2
b


c = [9,5,6,4,3,8,2,1]
c[0], c[-1] = c[-1], c[0]
c
