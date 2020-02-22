N = int(input())
S_dic = {}

for n in range(N):
    S = input()

    if S in S_dic:
        S_dic[S] += 1
    else:
        S_dic[S] = 1


# 最大のvalueを取得する
max_value = max(S_dic.values())

max_S_list = [k for k, v in S_dic.items() if v == max_value]
max_S_list = sorted(max_S_list)

for max_S in max_S_list:
    print(max_S)

