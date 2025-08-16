## 1-mashq
a = ["olma", 'anor',  'behi', 'uzum', 'banan']
print(a[2])

## 2
m = [4, 6, 8, 2, 0]
n = [1, 3, 5, 7, 9]
b = m +n
print(f"Umumiy ro‘yhat: {b}")

##3
royxat = [14,1,5,1,6]

first = royxat[0]
middle= royxat[len(royxat) //2]
last = royxat[-1]
new = [first, middle, last]
print(new)

##4
kino = ['Forest gamp', 'Forsaj', 'Sonik', 'Transformer', 'Real madrid']
toplam = tuple(kino)
print(toplam)

##5
d = ['Madrid', 'Milan', 'LONDON', 'Paris']
print("Paris" in d)

##6
k = [8, 9, 11, 14]
v = k * 2
print(v)

##7
n = [8, 9, 11, 14]
n[0], n[-1] = n[-1], n[0]
print(n)

##8
toplam = (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
print(toplam[3:8])

##9
rang = input("Enter colors: ")
t = rang.count("qizil")
print(t)

##10
animals = ('cat', 'dog', 'monkey', 'lion')
b = animals.index('lion')
print(b)

##11
t1 =(3, 1, 2)
t2 = (5, 6, 4)
t0 = t1 + t2
print(t0)

##12
my_list=[ 10, 20, 30]
tuple = (100,200,300)
l = len(my_list)
t = len(tuple)
print(l, t)

##13
t =(5, 6, 8, 9, 15, 56)
l1 = list(t)
print(l1)

##14
c1 = (5, 8,15, 20, 25, 30, 35, 40, 50)
c2 = min(c1)
c3 = max(c1)
print(c2, c3)

##15
words = ('Real madrid', 'barselona', "Manchester yunayted")
word = words[::-1]
print(word)        
