# https://atcoder.jp/contests/abc070/tasks/abc070_b

A, B, C, D = map(int, input().split())

if A >= C:
    start = A
else:
    start = C

if B >= D:
    end = D
else:
    end = B

ans = end - start
if ans < 0:
    ans = 0

print(ans)