# ダイクストラ法

# 始点sから各頂点への最短距離
# n: 頂点数, w: 辺の数, cost[u][v]: 辺uvのコスト（存在しない時はinf）
def dijkstra(s, n, w, cost):

    # 最短距離のリスト
    min_d_list = [float('inf')] * n
    min_d_list[s] = 0

    # 確定済み頂点のリスト
    is_decided_list = [False] * n

    while True:

        # 全ての頂点を確定させた場合終了
        if all(is_decided_list):
            break

        min_v = -1

        # 未確定の頂点の中から最小の距離の頂点をmin_vとする
        for i in range(n):

            # とりあえず、未確定の頂点を適当に1つ探す
            if (not is_decided_list[i]) and (min_v == -1):
                min_v = i

            # 未確定の頂点の中から、最小の距離の頂点を選ぶ
            elif (not is_decided_list[i]) and (min_d_list[i] < min_d_list[min_v]):
                min_v = i


        # 頂点を確定させる
        is_decided_list[min_v] = True


        # 確定した頂点から到達できる頂点それぞれについて、
        # 今確定した地点からの距離が、すでに書き込まれている値よりも小さければその値で距離を更新する
        for j in range(n):
            min_d_list[j] = min(min_d_list[j], min_d_list[min_v] + cost[min_v][j])

    return min_d_list


n, w = map(int, input().split())

cost = [[float('inf') for i in range(n)] for i in range(n)]

for i in range(w):
    x, y, z = map(int, input().split())
    cost[x][y] = z
    cost[y][x] = z

print(dijkstra(0, n, w, cost))


