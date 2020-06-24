# https://atcoder.jp/contests/abc136/tasks/abc136_a

A, B, C = map(int, input().split())

l = A - B

ans = C - l

if ans <= 0:
    ans = 0

print(ans)