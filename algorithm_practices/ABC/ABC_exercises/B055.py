# https://atcoder.jp/contests/abc055/tasks/abc055_b

N = int(input())
MOD = 10**9 + 7

power = 1
for i in range(1, N+1):
    power *= i
    power = power % MOD

print(power)
