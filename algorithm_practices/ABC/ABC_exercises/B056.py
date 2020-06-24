# https://atcoder.jp/contests/abc056/tasks/abc056_b

W, a, b = map(int, input().split())

if a < b and a+W < b:
    ans = abs(a+W - b)
elif b < a and b+W < a:
    ans = abs(b+W - a)
else:
    ans = 0

print(ans)