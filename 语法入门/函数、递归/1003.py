import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
p = int(str(t) + str(t)[-2::-1])
print("prime" if is_prime(p) else "noprime")
