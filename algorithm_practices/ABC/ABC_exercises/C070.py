# https://atcoder.jp/contests/abc070/tasks/abc070_c

# 最小公倍数を求める問題
# 参考：https://note.nkmk.me/python-gcd-lcm/
# https://www.planeta.tokyo/entry/3732/
# 上記リンク先に最大公約数も載ってた


# ユークリッドの互除法
# 例
# gcd(58585, 18184)
# = gcd(4033, 18184) (58585 = 18184 * 3 + 4033)
# = gcd(4033, 2052) (18184 = 4033 * 4 + 2052)
# = gcd(1981, 2052) (4033 = 2052 * 1 + 1981)
# = gcd(1981, 71) (2052 = 1981 + 71)
# = gcd(64, 71) (1981 = 71 * 27 + 64)
# = gcd(64, 7) (71 = 64 * 1 + 7)
# = gcd(1, 7) (64 = 7 * 9 + 1)
# = 1

N = int(input())
T = []
for i in range(N):
    T.append(int(input()))

def gcd(x, y):
    if x < y:
        x, y = y, x
    while x % y != 0:
        x, y = y, x % y
    return y


ans = T[0]
for i in range(1, N):
    ans *= T[i] // gcd(ans, T[i])

print(ans)


'''
# 2変数の最大公約数
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 2変数の最小公倍数
def lcm_base(x, y):
    x_y = x * y
    gcd_xy = gcd(x, y)
    ans = x_y // gcd_xy
    return ans

for i in range(1, N):
    T[i] = lcm_base(T[i-1], T[i])

print(T[N - 1])

'''




