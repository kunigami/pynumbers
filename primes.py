from random import randint
from exponentiation import modexp

# Return a list of primes less than N
def sieve (N):
    """Return a list of primes less than N"""
    isprime = [True]*(N)

    i = 2
    while (i*i < N):
        if isprime[i]:
            for j in range(i*i, N, i):
                isprime[j] = False
        i += 1

    return filter(lambda x: isprime[x], range(2,N))

# Decides whether a number is prime using the miller-rabin test
def miller_rabin(n, k=10):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in range (1, k):
        (s, d) = factor2(n - 1)
        a = randint(2, n-2)
        x = modexp(a, d, n)
        if x == 1 or x == n-1:
            continue
        sure = True
        for j in range(1, s):
            x = modexp(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                sure = False
                break
        if sure:
            return False
    return True

def factor2(n):
    d = 0
    while n % 2 == 0:
        n /= 2
        d += 1
    return (d, n)

# implementation selection
is_prime = miller_rabin


