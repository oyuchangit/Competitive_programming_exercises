# https://atcoder.jp/contests/abc076/tasks/abc076_c

S_ = input()    # ?入りの文字
T = input()     # 部分文字列
len_S_ = len(S_)
len_T = len(T)
S_list = []

for i in reversed(range(len_S_)):
    is_target = True
    S = ''

    # i番目の文字列からTに入れ替える
    if i + len_T <= len_S_:
        S = S_[:i] + T + S_[i + len_T:]

        for j in range(len(S)):
            # 入れ替えた文字列が条件1と矛盾しないか確認する
            if S[j] != S_[j] and S_[j] != '?':
                is_target = False
                break

            # 「?」をaにする(条件2)
            if S[j] == '?':
                S = S[:j] + 'a' + S[j + 1:]

        # 条件に合致する文字列を解の候補のリストに入れる
        if is_target:
            S_list.append(S)

    else:
        continue
        
if len(S_list) > 0:
    print(min(S_list))
else:
    print('UNRESTORABLE')