# https://atcoder.jp/contests/abc073/tasks/abc073_b

N = int(input())
d = 0

for i in range(N):
    l, r = map(int, input().split())
    d += (r - l + 1)

print(d)