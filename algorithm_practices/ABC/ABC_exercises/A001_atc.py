# https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

# 入力
H, W = map(int, input().split())
field = []

for i in range(H):
    line = input()
    field.append(list(line))

    s_x = line.find('s')
    if s_x != -1:
        start = [s_x, i]

# 深さ優先探索　塗りつぶし
# 現在位置(x, y)
def dfs (x, y):
    # (x, y)が壁か迷路の外なら移動不可
    if x < 0 or H <= x or y < 0 or W <= y or field[x][y] == '#':
        return
    
    # (x, y)がgoalである
    if field[x][y] == 'g':
        print('Yes')
        exit()
    
    # 到達地点を壁にする
    field[x][y] = '#'

    # 移動距離4方向
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx = x + dx
        ny = y + dy
        dfs(nx, ny)

dfs(start[1], start[0])
print('No')




# 以下REになるやつ　原因よくわかってない
'''
import numpy as np
import sys
sys.setrecursionlimit(500*500)

# 入力
H, W = map(int, input().split())
field = []

for i in range(H):
    field.append(list(input()))

field = np.array(field)

can_reach_goal = False

# 深さ優先探索　塗りつぶし
# 現在位置(x, y)
def dfs (x, y):
    # 今いるところを壁に置き換える
    field[x][y] = '#'

    # 移動距離4方向
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx = x + dx
        ny = y + dy

        # nxとnyが迷路の範囲内であるかどうかを判定
        if 0 <= nx < H and 0 <= ny < W:

            # (nx, ny)がgoalであるとき
            if field[nx][ny] == 'g':
                global can_reach_goal
                can_reach_goal = True
                return
            
            # field[nx][ny]が通り道である場合、再帰
            elif field[nx][ny] == '.':
                dfs(nx, ny)

index_of_s = np.where(field == 's')

dfs(index_of_s[0][0], index_of_s[1][0])

if can_reach_goal:
    print('Yes')
else:
    print('No')
'''