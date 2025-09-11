#1
def insert_underscores(txt):
    vowels = "aeiou"
    result = ""
    count = 0
    
    i = 0
    while i < len(txt):
        result += txt[i]
        count += 1
        
        if count == 3 and i != len(txt) - 1:
            if txt[i] in vowels or (i+1 < len(txt) and txt[i+1] == "_"):
                # keyingiga suramiz
                result += txt[i+1] + "_"
                i += 1
            else:
                result += "_"
            count = 0
        i += 1
    return result

# Testlar
print(insert_underscores("hello"))         # hel_lo
print(insert_underscores("assalom"))       # ass_alom
print(insert_underscores("abcabcabcdeabcdefabcdefg"))

#2
n = int(input("n = "))

for i in range(n):
    print(i ** 2)

#3
# Exercise 1
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# Exercise 3
num = int(input("Enter number: "))
total = 0
for i in range(1, num+1):
    total += i
print("Sum is:", total)


# Exercise 4
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)

# Exercise 5
numbers = [12, 75, 150, 180, 145, 525, 50]
for n in numbers:
    if n % 5 == 0 and n < 200:
        print(n)

# Exercise 6
num = int(input("Enter number: "))
print("Digits:", len(str(num)))

# Exercise 7
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# Exercise 8
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
    print(i)

# Exercise 9
for i in range(-10, 0):
    print(i)

# Exercise 10
for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11 (prime numbers)
start, end = 25, 50
print("Prime numbers between", start, "and", end, ":")
for num in range(start, end+1):
    if num > 1:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)

# Exercise 12 (Fibonacci)
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end=" ")
    a, b = b, a+b
print()

# Exercise 13 (Factorial)
n = int(input("Enter number: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"{n}! =", fact)

#4
def uncommon_elements(list1, list2):
    result = []
    for x in list1:
        if x not in list2:
            result.append(x)
    for y in list2:
        if y not in list1:
            result.append(y)
    return result

# Testlar
print(uncommon_elements([1, 1, 2], [2, 3, 4]))     
# [1, 1, 3, 4]

print(uncommon_elements([1, 2, 3], [4, 5, 6]))     
# [1, 2, 3, 4, 5, 6]

print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) 
# [2, 2, 5]
