'''     p. 35
深さ優先探索 (DFS: Depth-First Search) 

-Lake Counting (POJ No.2386)-
大きさがN×Mの庭があります。そこに雨が降り、水たまりができました。
水たまりは8近傍で隣接している場合につながっているとみなします。
全部でいくつの水たまりがあるでしょうか？
（8近傍とは、次のWに対する*の部分を指します。）

***
*W*
***

-制約-
・N, M <= 100

-例-
入力
N = 10, M = 12
庭は次図（'W'は水たまりを、'.'は水たまりでないところを表します。）

W........WW.
.WWW.....WWW
....WW...WW.
.........WW.
.........W..
.........W..
..W......W..
.W.W.....WW.
W.W.W.....W.
..W.......W.

出力
3
'''


import time
import numpy as np


# 入力
N, M = map(int, input().split())
field = []

for l in range(N):
    field.append(list(input()))

field = np.array(field)


# 現在位置(x, y)
def dfs(x, y):
    # 今いるところを.に置き換える
    field[x][y] = '.'

    # 移動する8方向をループ
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            # x方向にdx, y方向にdy移動した場所を(nx, ny)とする
            nx = x + dx
            ny = y + dy
            # nxとnyが庭の範囲かどうかとfield[nx][ny]が水たまりかどうかを判定
            if 0 <= nx < N \
                and 0 <= ny <= M-1 \
                and field[nx][ny] == 'W':

                dfs(nx, ny)




# 時間計測用 開始時間
_start_time = time.time()


lake_count = 0
for n in range(N):
    for m in range(M):

        if field[n][m] == 'W':
            # Wが残っているならそこからdfsを始める
            dfs(n, m)
            lake_count += 1

print(lake_count)


# 時間計測用 実行時間
_elapsed_time = time.time() - _start_time
print(_elapsed_time * 1000)

        



