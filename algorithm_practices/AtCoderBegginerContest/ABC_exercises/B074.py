# https://atcoder.jp/contests/abc074/tasks/abc074_b

N = int(input())
K = int(input())
x_list = list(map(int, input().split()))

ans = 0
for x in x_list:
    K_x = K - x

    if K_x >= x:
        ans += x*2

    elif K_x < x:
        ans += K_x*2

print(ans)