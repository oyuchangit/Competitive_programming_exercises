# https://atcoder.jp/contests/abc146/tasks/abc146_c

A, B, X = map(int, input().split())

min_val = 1
max_val = 1000000000
mid_val = (min_val + max_val) // 2
count = 0

if A * 1000000000 + B * 10 < X:
    print(1000000000)
    exit()

elif A * 1 + B * 1 > X:
    print(0)
    exit()

while True:
    if count ==10000000:
        break

    mid_val = (min_val + max_val) // 2
    mid_price = A * mid_val + B * (len(str(mid_val)))

    if (X == mid_price):
        print(mid_val)
        exit()
    elif (max_val - min_val == 1):
        print(min_val)
        exit()
    elif X > mid_price:
        min_val = mid_val
    else:
        max_val = mid_val

    count += 1
