# https://atcoder.jp/contests/abc075/tasks/abc075_c

import copy
import itertools

# N頂点M辺
N, M = map(int, input().split())

# グラフのリスト　各頂点からどこの頂点に向かって辺が伸びてるかという情報
graph_list = [[] for i in range(N)]
a_b_list = []

for i in range(M):
    a, b = map(int, input().split())
    a_b_list.append([a - 1, b - 1])
    graph_list[a - 1].append(b - 1)
    graph_list[b - 1].append(a - 1)

# グラフのDFS
def dfs(current, graph_list, visited):

    for j in graph_list[current]:
        if visited[j] == False:
            # 現在地を書き込む
            visited[j] = True
            # 次の頂点に移動する
            dfs(j, graph_list, visited)

    # 全ての頂点を通ったかどうか判定
    if all(visited):
        return True
    else:
        return False


# 橋の数
count_bridge = 0

for m in range(M):
    graph_list_tmp = copy.deepcopy(graph_list)

    a = a_b_list[m][0]
    b = a_b_list[m][1]

    graph_list_tmp[a].pop(graph_list_tmp[a].index(b))
    graph_list_tmp[b].pop(graph_list_tmp[b].index(a))

    # 頂点を通ったかどうか
    visited = [False] * N
    visited[0] = True
    result = dfs(0, graph_list_tmp, visited)

    if result != True:
        count_bridge += 1

print(count_bridge)




    # tmp_a_b_list = copy.copy(a_b_list)
    # tmp_a_b_list.pop(m)
    # 2次元配列を1次元化（平坦化）
    # tmp_a_b_list = set(itertools.chain.from_iterable(tmp_a_b_list))
    # if tmp_a_b_list != compari_list:
    #     ans += 1


    # 頂点から1方向にしか辺が伸びていないものの数
    # count_single = 0

    # for g in graph_list_tmp:
    #     if len(g) <= 1:
    #         count_single += 1

    # if count_single > 2:
    #     count_bridge += 1






