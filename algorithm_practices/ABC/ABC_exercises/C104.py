# https://atcoder.jp/contests/abc104/tasks/abc104_c

D, G = map(int, input().split())

p = []  # 各点数台の問題数のリスト
c = []  # 各点数台のコンプリートボーナス

# 各点数台を、完全に解くかどうかのリスト　1問も解かないとして初期化
solve_completely_list = [False] * D

# 入力処理
for d in range(D):
    p_i, c_i = map(int, input().split())
    p.append(p_i)
    c.append(c_i)


def dfs(i, solve_completely_list, completed_amount_list):
    if i >= D:
        is_larger_than_G = False    # フラグ初期化
        # total_score計算
        total_score = 0
        completed_amount = 0
        for d in range(D):
            if solve_completely_list[d]:
                total_score += (d+1) * 100 * p[d] + c[d]
                completed_amount += p[d]


        # total_scoreがGより小さいとき
        # Gより大きくなるまで、一番大きい配点を足す
        # 一番大きい配点をp-1個足してもGより小さい場合、諦めて他の枝に移る
        if total_score < G:
            # solve_completely_list[D]がTrueのときは、(D-1) * 100を最大の配点とする
            # solve_completely_list[i]がFalseであるiのうち最大のiの配点を使う
            max_d = -1
            for d_i in reversed(range(D)):
                if solve_completely_list[d_i] == False:
                    max_d = d_i
                    break
            # 多分ありえないけど一応
            if max_d == -1:
                return

            for p_d in range(p[max_d] - 1):
                total_score += (max_d + 1) * 100
                completed_amount += 1
                if total_score >= G:
                    is_larger_than_G = True
                    break
        else:
            is_larger_than_G = True
        
        if is_larger_than_G:
            completed_amount_list.append(completed_amount)
        return
    

    # 完全に解く(100i 点の問題を pi 問解く)場合
    solve_completely_list[i] = True
    dfs(i + 1, solve_completely_list, completed_amount_list)

    # 1問も解かない場合
    solve_completely_list[i] = False
    dfs(i + 1, solve_completely_list, completed_amount_list)

completed_amount_list = []    # 回答した数のリスト
dfs(0, solve_completely_list, completed_amount_list)
print(min(completed_amount_list))

