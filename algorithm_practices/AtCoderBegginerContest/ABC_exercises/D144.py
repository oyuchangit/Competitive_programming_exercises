# https://atcoder.jp/contests/abc144/tasks/abc144_d

import math

a, b, x = map(int, input().split())

w_max = a * a * b

# 対角線の水量
w_middle = w_max / 2

degree = 0

# 対角線以下の水量の時
if x <= w_middle:
    degree = math.degrees(math.atan((a*(b**2)) / (2*x)))

else:
    degree = math.degrees(math.atan(((w_max - x)*2) / (a**3)))

print(degree)
