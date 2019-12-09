N = int(input())

x_list = []
y_list = []

# 証言の数のリスト
A_list = []


# 入力処理
for n in range(N):
    # 各人が持ってる証言の数
    A = int(input())
    A_list.append(A)
    x = []
    y = []
    for a in range(A):
        x_tmp, y_tmp = map(int, input().split())
        x.append(x_tmp)
        y.append(y_tmp)
    x_list.append(x)
    y_list.append(y)


# 正直者（仮定）のリスト
# Falseで初期化　みんな不親切だと仮定する
isHonest_list = [False] * N

# 解候補のリスト
ans_candidate = []

# 全探索
def dfs(i, isHonest_list, ans_candidate):
    # 正直者・不親切の仮定が矛盾しないかどうか判定する
    # 矛盾しない場合、解候補のリストに正直者の人数を追加する
    if i >= N:
        isNotContradict = True  # 矛盾しないと仮定する
        for n in range(N):
            # 人iが不親切という仮定のときは証言を考慮しない
            if isHonest_list[n] == False:
                continue
            # 正直（仮定）な人iの各証言を考慮
            for A_list_i in range(A_list[n]):
                # 正直な人（仮定）なのに不親切な人のことを正直者、
                # もしくは正直者のことを不親切と証言してたら矛盾する
                if (y_list[n][A_list_i] == 1 and isHonest_list[x_list[n][A_list_i]-1] == False) or\
                    (y_list[n][A_list_i] == 0 and isHonest_list[x_list[n][A_list_i]-1]):
                    isNotContradict = False
                    break
            else:
                continue
            break

        # 矛盾しないとき
        if isNotContradict:
            # 解候補のリストに正直者の人数を追加する
            ans_candidate.append(isHonest_list.count(True))
        return

    # 不親切な人であると仮定する
    isHonest_list[i] = False
    dfs(i+1, isHonest_list, ans_candidate)
    
    # 正直者であると仮定する
    isHonest_list[i] = True
    dfs(i+1, isHonest_list, ans_candidate)

dfs(0, isHonest_list, ans_candidate)
print(max(ans_candidate))



# 以下本番中に書いたif文地獄
# 不親切な人のことを嘘つきだと思ってしまった

'''
for i in range(N):
    for A_list_i in range(A_list[i]):

        # 指名された人のGroup
        Group_mentioned = Group[x_list[i][A_list_i]-1]

        # 人iのA個目の証言が、誰かが正直者であるという内容のとき
        if y_list[i][A_list_i] == 1:
            
            # 人iのGroupと指名された人のGroupがまだ未分類のとき
            # 両方ともGroup1に振り分ける
            if Group[i] == Group_none and Group_mentioned == Group_none:
                Group[i] = Group_1
                Group[x_list[i][A_list_i]-1] = Group_1
            
            # 人iのGroupもしくは指名された人のGroupのどちらか一方は未分類かつ
            # もう片方は分類済みのとき
            # 未分類の方を分類済みのGroupと同じにする
            elif Group[i] != Group_mentioned and Group[i] == Group_none:
                Group[i] = Group_mentioned
            elif Group[i] != Group_mentioned and Group_mentioned == Group_none:
                Group[x_list[i][A_list_i]-1] = Group[i]

            # 人iのGroupと指名された人のGroupが違う、かつ
            # 人iと指名された人がともに分類済みであるとき
            # 矛盾するので、正直者は存在しない
            elif Group[i] != Group_mentioned and Group[i] != Group_none and Group_mentioned != Group_none:
                has_no_honest = True
                break
        
        # 人iのA個目の証言が、誰かが嘘つきであるという内容のとき
        if y_list[i][A_list_i] == 0:

            # 人iのGroupと指名された人のGroupがまだ未分類のとき
            # 人iはGroup1、指名された人はGroup2に分類する
            if Group[i] == Group_none and Group_mentioned == Group_none:
                Group[i] = Group_1
                Group[x_list[i][A_list_i]-1] = Group_2

            # 人iのGroupもしくは指名された人のGroupのどちらか一方は未分類かつ
            # もう片方は分類済みのとき
            # 未分類の方を分類済みのGroupと違うGroupにする
            elif Group[i] != Group_mentioned and Group[i] == Group_none:
                if Group_mentioned == Group_1:
                    Group[i] = Group_2
                else:
                    Group[i] = Group_1
            elif Group[i] != Group_mentioned and Group_mentioned == Group_none:
                if Group[i] == Group_1:
                    Group[x_list[i][A_list_i]-1] = Group_2
                else:
                    Group[x_list[i][A_list_i]-1] = Group_1

            # 人iのGroupと指名された人のGroupが同じ、かつ
            # 人iと指名された人がともに分類済みであるとき
            # 矛盾するので、正直者は存在しない
            elif Group[i] == Group_mentioned and Group[i] != Group_none and Group_mentioned != Group_none:
                has_no_honest = True
                break
    else:
        continue
    break


if has_no_honest:
    print(0)
else:
    print(max(Group.count(Group_1), Group.count(Group_2)))
'''

          
