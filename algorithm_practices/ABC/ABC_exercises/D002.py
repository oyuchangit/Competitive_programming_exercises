# https://atcoder.jp/contests/abc002/tasks/abc002_4

# 国会議員の数, 人間関係の数
N, M = map(int, input().split())

x_y_list = []    # 人間関係のリスト
for m in range(M):
    x, y = map(int, input().split())
    x_y_list.append([x, y])

# 派閥に入れる人のリスト 一人も入れない設定で初期化
is_member_list = [False] * N

# 矛盾しない場合の派閥の人数のリスト　解の候補リスト
correct_number_of_member_list = []

def dfs(i, is_member_list, correct_number_of_member_list):
    # 議員を派閥に入れるかどうかN人分決め終わったときの処理
    if i >= N:          
        '''
        正しい派閥の人間関係は以下のようになる
        議員A、B、Cがメンバーの場合
        ・A、Bが知り合い
        ・B、Cが知り合い
        ・C、Aが知り合い
        の3通りあればよい
        三人メンバーがいれば、メンバー同士の人間関係は3通り必要
        人間関係のうち、メンバー同士のものを抽出して、その数が、
        メンバーの数 × (メンバーの数-1) × 1/2 個あればよいはず
        ※メンバーの人間関係のリストに重複がないことが前提
        '''
        count_x_y_of_member = 0

        # 人間関係x, yのうち、両方とも派閥のメンバーに言及しているものの数を数える
        for j in range(M):
            if is_member_list[x_y_list[j][0] - 1] and is_member_list[x_y_list[j][1] - 1]:
                count_x_y_of_member += 1
        
        # メンバー同士の人間関係の数が正しい場合、そのメンバーの数を解の候補に入れる
        number_of_member = is_member_list.count(True)
        if count_x_y_of_member == number_of_member * (number_of_member - 1) / 2:
            correct_number_of_member_list.append(number_of_member)

        return

    # 議員iを派閥に入れる場合
    is_member_list[i] = True
    dfs(i + 1, is_member_list, correct_number_of_member_list)

    # 議員を派閥に入れない場合
    is_member_list[i] = False
    dfs(i + 1, is_member_list, correct_number_of_member_list)

dfs(0, is_member_list, correct_number_of_member_list)
print(max(correct_number_of_member_list))
