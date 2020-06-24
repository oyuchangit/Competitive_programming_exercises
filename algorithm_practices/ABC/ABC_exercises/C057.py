# https://atcoder.jp/contests/abc057/tasks/abc057_c
import numpy as np

N = int(input())
A = int(np.sqrt(N))

while A > 0:
    if N %  A == 0:
        B = N / A
        break
    else:
        A -= 1

digit_count = 0

while B >= 1:
    digit_count += 1    
    B /= 10

print(digit_count)