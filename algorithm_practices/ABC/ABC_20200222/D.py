n, a, b = map(int, input().split())

# 繰り返し二乗法
def mod_pow(x, n, p):
    if n == 1:
        return x % p
    elif n % 2 == 1:
        return (x * mod_pow(x, n - 1, p)) % p
    else:
        t = mod_pow(x, n / 2, p)
        return t ** 2 % p


ans = mod_pow(2, n, 10 ** 9 + 7)
print(ans)

