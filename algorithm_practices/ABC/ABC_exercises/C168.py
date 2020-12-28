# https://atcoder.jp/contests/abc168/tasks/abc168_c

import math


# A: 時針の長さ B: 分針の長さ 
# H時M分
A, B, H, M = map(int, input().split())


# AとBの間の角度
A_degree = H*60*(1/360) + M*(1/360)
B_degree = M*(1/30)
AB_degree = abs((A_degree - B_degree)) * math.pi

if AB_degree >= math.pi:
    AB_degree = 2*math.pi - AB_degree


# 余弦定理
d = math.sqrt(A**2 + B**2 - 2*A*B * math.cos(AB_degree))

print(d)

