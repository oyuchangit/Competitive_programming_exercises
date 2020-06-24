# https://atcoder.jp/contests/abc135/tasks/abc135_b

N = input()
p = list(map(int, input().split()))

count = 0

for i, p_i in enumerate(p):
    if (i+1) != p_i:
        count += 1

if count == 2 or count == 0:
    print('YES')
else:
    print('NO')