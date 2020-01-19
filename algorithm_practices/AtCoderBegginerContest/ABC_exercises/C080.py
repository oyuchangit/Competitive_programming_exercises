# https://atcoder.jp/contests/abc080/tasks/abc080_c

# 各店の各曜日の各営業時間で営業するかどうか全探索


N = int(input())    # 店の数
F_list = []
for _ in range(N):
    f = list(map(int, input().split()))
    F_list.append(f)

P_list = []
for _ in range(N):
    p = list(map(int, input().split()))

is_joisino_shop_open_list = []

# 各曜日時間帯の最低限の店の開店数（おねーちゃんの店を考慮しない）
min_open_list = []
for i in range(10):
    count_open = 0
    for j in range(N):
        if F_list[i][j] == 1:
            count_open += 1
        min_open_list.append(count_open)

# c個の店が営業中の時の、店iの利益
def benefit(i, c):
    return P_list[i][c]

def dfs():
    if j > 10:
        if True in is_joisino_shop_open_list:            
            # joisinoおねえちゃんのお店の利益を計算
            benefit_joisino = 0
            for i in range(10):
                # お店の開店数
                count_open = min_open_list[i]
                if is_joisino_shop_open_list[i]:
                    count_open += 1
                benefit_joisino += benefit(i, count_open)

    # j




