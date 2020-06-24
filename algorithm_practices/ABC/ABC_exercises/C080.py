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
    P_list.append(p)

# c個の店が営業中の時の、店iの利益
def benefit(i, c):
    return P_list[i][c]

is_joisino_shop_open_list = [False] * 10
benefit_joisino_list = []

def dfs(j):
    if j >= 10:

        # 1つ以上の時間帯でお店を営業していること
        if True in is_joisino_shop_open_list:
            # joisinoおねえちゃんのお店の利益を計算
            benefit_joisino = 0
            for n in range(N):
                # 各お店ごとのjoisinoお姉ちゃんの利益を計算
                count_n_open = 0                
                shop_n_list = F_list[n]

                for i in range(10):    
                    if shop_n_list[i] == 1 and is_joisino_shop_open_list[i] == True:
                        count_n_open += 1

                benefit_n_joisino = P_list[n][count_n_open]
                benefit_joisino += benefit_n_joisino

            benefit_joisino_list.append(benefit_joisino)

        return

    # joisinoお姉ちゃんのお店をあけるかあけないか全パターン試す
    # j番目の日時にjoisinoお姉ちゃんのお店をあけるとき
    is_joisino_shop_open_list[j] = True
    dfs(j+1)

    # j番目の日時にjoisinoお姉ちゃんのお店をあけないとき
    is_joisino_shop_open_list[j] = False
    dfs(j+1)


dfs(0)
max_benefit_joisino = max(benefit_joisino_list)
print(max_benefit_joisino)
