##1 
#year = int(input())
def is_leap(year):
    """
    Determines whether a given year is a leap year.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.
    """
   # for is_leap in year:
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Test
#print(is_leap(2024))  # True
#print(is_leap(1900))  # False
print(is_leap(2000))  # True



##2
a = int(input('a = '))

if a % 2 != 0:
    print('Weird')
elif a % 2 == 0 and 2 <= a <= 5:
    print('Not Weird')
elif a % 2 == 0 and 6 <= a <= 20:
    print('Weird')
elif a % 2 == 0 and 20 <= a <= 100:
    print('Not Weird')



##3
a = int(input('a = '))
b = int(input('b = '))

s = a if a % 2 == 0 else a +1

if s <= b:
    print(list(range(s, b +1, 2)))
else:
    print([])
