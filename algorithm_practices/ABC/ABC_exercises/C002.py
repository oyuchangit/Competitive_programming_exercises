# https://atcoder.jp/contests/abc002/tasks/abc002_3

x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())

# (x_a, y_a)を原点に移動して他の2点もずらす
x_b -= x_a
y_b -= y_a
x_c -= x_a
y_c -= y_a

# 面積を計算
area = abs(x_b * y_c - y_b * x_c) / 2

print(area)