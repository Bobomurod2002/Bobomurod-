## 1

d = {1:2, 3: 4, 5: 6}
m = dict(sorted(d.items())),
key = lambda x: x[1]

n = dict(sorted(d.items(), key =lambda x: x[1], reverse= True))
print("O'sish tartibi:", m)

print("Kamayish tartibi:", m)


##2
d = {0: 10, 1: 20}

d[2] = 30
print(d)


##3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4={**dic1, **dic2, **dic3}
print(dic4)


##4 
n = 5

d1= {x: x*x for x in range(1, n+1)}
print(d1)


## 5
n = int(input('n ni kirit'))

d1= {x: x*x for x in range(1, n+1)}
print(d1)


## set homework 1
my_list = [1, 2, 2, 3, 4, 4, 5, 7,7,7,8]
my_set = set(my_list)
print(my_set)

#2  --- To‘plam Elementlarini Aylantirib Chiqish (Iteratsiya)
set = {1, 2,4,3, 5, 6, 7, 7, 8, 9, 20  }

for m in set:
    print(m)

##3 toplamga element qoshish
my_set = {1, 2, 3, 4, 5, 7, 8}
my_set.add(6)
print(my_set)


##4 toplamdan element ochirish
my_set = {1, 2, 3, 4, 5, 7, 8}
my_set.remove(8)
print(my_set)


##5

my_set = {1, 2, 3, 4, 5, 7, 8}
my_set.discard(8)
print(my_set)

