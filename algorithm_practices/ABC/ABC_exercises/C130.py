# https://atcoder.jp/contests/abc130/tasks/abc130_c

W, H, x, y = map(int, input().split())

num = 0
if x == W/2 and y == H/2:
    num = 1

print(W * H / 2, num)