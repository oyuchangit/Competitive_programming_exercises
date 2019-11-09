'''     p. 37
幅優先探索 (BFS: Breadth-First Search)

-迷路の最短路-

大きさがN×Mの迷路が与えられます。迷路は通路と壁からできており、
１ターンに隣接する上下左右４マスの通路へ移動することができます。
スタートからゴールまで移動するのに必要な最小のターン数を求めなさい。
ただし、スタートからゴールまで移動できると仮定します。

制約
・N, M <= 100

例
入力
N = 10, M = 10

#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#


出力
22
'''

import numpy as np
import queue as que

INF = 100000000

# 入力
N = int(input())
M = int(input())
maze = []
for n in range(N):
    maze.append(list(input()))

maze = np.array(maze)
start = np.where(maze == 'S')   # スタート地点の座標
goal = np.where(maze == 'G')    # ゴール地点の座標

min_d = []      # 各点までの最短距離の配列

# 移動4方向のベクトル
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


# スタートからゴールへの最短距離を求める
# たどりつけないとINF
def bfs():
    # 全ての点をINFで初期化
    min_d = np.full((N, M), INF)

    # スタート地点をキューに入れて、その点の距離を0にする
    q = que.Queue()
    q.put(start)
    min_d[start[0], start[1]] = 0

    # キューが空になるまでループ
    while not q.empty():
        # キューの先頭を取り出す
        front_q = q.get()
        # 取り出した状態がゴールなら探索をやめる
        if front_q[0] == goal[0] and front_q[1] == goal[1]:
            break
        # 移動4方向をループ
        for i in range(4):
            # 移動した後の点を(nx, ny)とする
            nx = front_q[0] + dx[i]
            ny = front_q[1] + dy[i]

            # 移動が可能かの判定とすでに訪れたことがあるかの判定
            # min_d[ny, nx] != INFなら訪れたことがある
            if 0 <= nx \
                and nx < N \
                and 0 <= ny \
                and ny < M \
                and maze[nx, ny] != '#' \
                and min_d[nx, ny] == INF:

                # 移動できるならキューに入れ、その点の距離をキューの先頭 +1 で確定する
                q.put([nx, ny])
                min_d[nx, ny] = min_d[front_q[0], front_q[1]] + 1
        
    return min_d[goal[0], goal[1]]
        

result = bfs()
print(result[0])