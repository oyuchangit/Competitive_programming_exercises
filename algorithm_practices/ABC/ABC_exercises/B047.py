# https://atcoder.jp/contests/abc047/tasks/abc047_b

import numpy as np

W, H, N = map(int, input().split())

x_list = []
y_list = []
a_list = []

field = np.ones((H, W), dtype=np.int)

for i in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        for i in range(x):
            for j in range(H):
                field[j, i] = 0
    elif a == 2:
        for i in range(x, W):
            for j in range(H):
                field[j, i] = 0
    elif a == 3:
        for i in range(y):
            for j in range(W):
                field[i, j] = 0
    elif a == 4:
        for i in range(y, H):
            for j in range(W):
                field[i, j] = 0

print(np.count_nonzero(field == 1))
    



