# https://atcoder.jp/contests/arc029/tasks/arc029_1

# 入力
N = int(input())    # おにくの数
t_list = []         # それぞれのおにくを焼くのにかかる時間のリスト
for i in range(N):
    t = int(input())
    t_list.append(t)

# 肉焼き器A, Bのうち、Aで焼くかどうかのリスト
# Trueの場合肉焼き器Aで焼く Falseの場合肉焼き器Bで焼く
is_bake_on_A_list = [True] * N  # 全部Aで焼く体で初期化

time_required_list = [] # おにくを焼くのにかかる時間のリスト
def dfs(i, is_bake_on_A_list, time_required_list):
    if i >= N:
        # おにくが焼き終わるまでの時間を計算
        A_time_required = 0
        B_time_required = 0
        for i in range(N):
            if is_bake_on_A_list[i]:
                A_time_required += t_list[i]
            else:
                B_time_required += t_list[i]

        # お肉焼くのにかかる時間 after all       
        time_required = max(A_time_required, B_time_required)
        time_required_list.append(time_required)

        return

    # おにくをAで焼く
    is_bake_on_A_list[i] = True
    dfs(i + 1, is_bake_on_A_list, time_required_list)

    # おにくをBで焼く
    is_bake_on_A_list[i] = False
    dfs(i + 1, is_bake_on_A_list, time_required_list)


dfs(0, is_bake_on_A_list, time_required_list)
print(min(time_required_list))