'''
-動的計画法-

重さと価値がそれぞれw_i, v_iであるようなn個の品物があります。
これらの品物から、重さの総和がWを超えないように選んだときの、価値の総和を求めなさい。

-制約-
・1 <= n <= 100
・1 <= w_i, v_i <= 100
・1 <= W <= 10000

-入力-
・n = 4
・(w, v) = {(2, 3), (1, 2), (3, 4), (2, 2)}
・W = 5

4
5
2 3
1 2
3 4
2 2
'''

import numpy as np

# 入力
n = int(input())
W = int(input())
w_v = []
dp = np.full((n + 1, W + 1), 0)

for i in range(n):
    w, v = map(int, input().split())
    w_v.append([w, v])


# 動的計画法
for j in range(n):
    for k in range(W + 1):
        if k < w_v[j][0]:
            dp[j + 1][k] = dp[j][k]
        else:
            dp[j + 1][k] = max(dp[j][k], dp[j][k - w_v[j][0]] + w_v[j][1])

print(dp[n][W])