# https://atcoder.jp/contests/abc048/tasks/abc048_b

a, b, x = map(int, input().split())

if a == 0:
    print(b // x + 1)

elif a == 1:
    print(b // x)

else:
    print(b//x - (a-1)//x)
