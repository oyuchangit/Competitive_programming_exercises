# https://atcoder.jp/contests/abc061/tasks/abc061_b

N, M = map(int, input().split())

# 各都市から、どこの都市に道路が伸びているかという情報
graph_list = [[] for i in range(N)]

for m in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph_list[a].append(b)
    graph_list[b].append(a)


for i in range(N):
    print(len(graph_list[i]))
    