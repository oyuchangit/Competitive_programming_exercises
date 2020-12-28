# https://atcoder.jp/contests/abc168/tasks/abc168_d

# グラフ
# 隣接リスト
# よくわからない

import sys
from collections import deque

N, M = map(int, input().split())
AB_adj = [[] for _ in range(N+1)] # ABの隣接リスト（adjacency list）



for i in range(M):
    A, B = map(int, input().split())
    AB_adj[A].append(B)
    AB_adj[B].append(A)


ans = [0] * (N+1)
ans[1] = 1
que = deque([1])

while que:
    A = que.popleft()
    
    for B in AB_adj[A]:
        if ans[B] == 0:
            ans[B] = A
            que.append(B)

print('Yes')

for i in range(2, N + 1):
    print(ans[i])