# https://atcoder.jp/contests/abc143/tasks/abc143_a

A, B = map(int, input().split())

ans = A - B*2

if ans <= 0:
    ans = 0
print(ans)