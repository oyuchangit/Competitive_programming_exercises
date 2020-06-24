# https://atcoder.jp/contests/abc133/tasks/abc133_c

L, R = map(int, input().split())

if (R - L) >= 2019:
    print(0)
    exit()

min_m = 2019

for i in range(L, R):
    for j in range(i + 1, R + 1):
        m = (i * j) % 2019

        min_m = min(min_m, m)

print(min_m)