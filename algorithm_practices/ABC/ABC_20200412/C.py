# 天才の回答
import math
k = int(input())
s = 0
box = [0]*(k+1)
for l in range (1,k+1):
     for m in range (1, k+1):
          box[math.gcd(l,m)] += 1

for l in range (1,k+1):
     for n in range (1, k+1):
          s += math.gcd(l,n)*box[l]

print(s)






# def gcd(x, y):
#     if x < y:
#         x, y = y, x
#     while x % y != 0:
#         x, y = y, x % y
#     return y


# def gcd_3(x, y, z):
#     x_y = gcd(x, y)
#     return gcd(x_y, z)

# from math import gcd


# K = int(input())
# ans = 0

# sum_list = []


# for i in range(1, K + 1):
#     for j in range(1, K + 1):
#         for k in range(1, K + 1):
#             ans += gcd(gcd(i, j), k)

# print(ans)