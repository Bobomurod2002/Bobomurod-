#1
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(10))  # False
print(is_prime(7))  # True

#2
def digit_sum(k):
    return sum(int(digit) for digit in str(k))
print(digit_sum(28))   # 6  (2 + 4)
print(digit_sum(502))  # 7  (5 + 0 + 2)



#3

def powers_of_two(N):
    power = 1
    while (2 ** power) <= N:
        print(2 ** power, end=' ')
        power += 1
powers_of_two(20)
