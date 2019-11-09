'''
import math
def trial_division(n):
    """Return a list of the prime factors for a natural number."""
    if n < 2:
        return []
    prime_factors = []
    for p in range(1, int(n**0.5)+1):
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors


N = int(input())
prime_factors = trial_division(N)
prime_factors.sort()
len_prime_factors = len(prime_factors)

a = 1
b = 1
for i in range(0, len_prime_factors, 2):
    a *= prime_factors[i]
    b *= prime_factors[i + 1]

a_b = a + b
print(a_b-2)
'''



N = int(input())

min_total = 100000000000000
for a in range(1, N // 2 + 2):
    b = N / a
    if b.is_integer():
        tmp_a_and_b = a + b
        if tmp_a_and_b < min_total:
            min_total = tmp_a_and_b

print(int(min_total - 2))

            