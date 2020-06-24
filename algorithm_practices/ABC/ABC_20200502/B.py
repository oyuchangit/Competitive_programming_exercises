import numpy as np
import math

X = int(input())
a = 100
count = 0

while True:
    a = math.floor(a * 1.01)

    count += 1

    if a >= X:
        print(count)
        exit()