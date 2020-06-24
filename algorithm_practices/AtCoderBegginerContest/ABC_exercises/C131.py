# https://atcoder.jp/contests/abc131/tasks/abc131_c

from fractions import gcd


A, B, C, D = map(int, input().split())

C_ = B // C
D_ = B // D

C_a = (A-1) // C
D_a = (A-1) // D

# 最小公倍数
CD = (C * D) // gcd(C, D)    # C*D / (最大公約数)

CD_ = (B // CD)
CD_a = ((A-1) // CD)

ans = B - (A-1) - (C_ - C_a) - (D_ - D_a) + (CD_ - CD_a)

print(int(ans))