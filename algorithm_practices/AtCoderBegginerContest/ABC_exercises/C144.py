# https://atcoder.jp/contests/abc144/tasks/abc144_c

import math

N = int(input())

mi = -1

for i in range(1, int(math.sqrt(N)) + 1):
    a = i
    if N % a != 0:
        continue

    b = N // a
    count = a + b - 2
    
    if mi <= -1 or mi > count:
        mi = count

print(mi)



