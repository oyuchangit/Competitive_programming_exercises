'''
p. 43
貪欲法 (Greedy algorithm) 

-区間の問題-
n個の仕事があります。各仕事は時間s_iに始まり、時間t_iに終わります。
あなたは各仕事について、参加するか参加しないかを選ばなければなりません。
仕事に参加するならば、その仕事の初めから終わりまで参加しなければなりません。
また、参加する仕事の時間帯が重なってはなりません（開始の瞬間・終了の瞬間だけが重なるのも許されません）。

できるだけ多くの仕事に参加したいです。何個の仕事に参加することができるでしょうか。

-制約-
・1 <= N <= 100000
・1 <= s_i <= t_i <= 10^9

-例-
入力
N = 5, s = {1, 2, 4, 6, 8}, t = {3, 5, 7, 9, 10}

5
1 3
2 5
4 7
6 9
8 10

出力
3
'''

import numpy as np

# 入力
N = int(input())

itv = []
range_N = range(N)
for i in range_N:
    s, t = map(int, input().split())
    itv.append([t, s])

# 2次元配列を辞書順でソート
itv = sorted(itv, key=lambda x:(x[0], x[1]))

ans = 0
t = 0

for i in range_N:
    if t < itv[i][1]:
        ans += 1
        t = itv[i][0]

print(ans) 