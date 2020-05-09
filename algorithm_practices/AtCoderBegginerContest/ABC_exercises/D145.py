# https://atcoder.jp/contests/abc145/tasks/abc145_d

X, Y = map(int, input().split())
p = 10 ** 9 + 7

if (X + Y)%3 != 0:
    print(0)
    exit()

n = (2*X - Y) / 3
m = (2*Y - X) / 3

if n < 0 or m < 0:
    print(0)
    exit()


# 2項係数
def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0

    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p

p = 10 ** 9 + 7
N = 10 ** 6


# 二項係数　高速
# https://www.planeta.tokyo/entry/5195/
# 階乗の配列 i番目の項目はi!
fact = [1, 1]

# 逆元の配列 i番目の項目は(i!)^(-1)
factinv = [1, 1]

# 逆元計算用の配列 i番目の項目は
# mod pを法とし、iの逆元((i)^(-1))
inv = [0, 1]

for i in range(2, N+1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

print(cmb(int(n + m), int(m), p))
