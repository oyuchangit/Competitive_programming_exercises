# https://atcoder.jp/contests/abc060/tasks/abc060_b

A, B, C = map(int, input().split())

for b in range(1, B+1):
    if (A * b) % B == C:
        print('YES')
        exit()

print('NO')


# 数学