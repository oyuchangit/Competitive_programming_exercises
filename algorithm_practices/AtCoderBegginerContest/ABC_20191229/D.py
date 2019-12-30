# N 回じゃんけんを行う,  K 回前のじゃんけんで出した手と同じ手を出すことはできない
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

# mod_N_list = [[] for i in range(K)]
# T_list = [[] for i in range(K)]
# T_list = []
# N_list = list(range(N))

ans = 0

for i in range(N):
    if T[i] == 'r':
        # 前回がrでは無かった時
        if i < K or T[i - K] != 'r':
            ans += P
        else:
            T = T[:i] + 'x' + T[i + 1:]

    elif T[i] == 's':
        # 前回がsでは無かった時
        if i < K or T[i - K] != 's':
            ans += R
        else:
            T = T[:i] + 'x' + T[i + 1:]

    elif T[i] == 'p':
        # 前回がpでは無かった時
        if i < K or T[i - K] != 'p':
            ans += S
        else:
            T = T[:i] + 'x' + T[i + 1:]

print(ans)
# print(T)


'''
for i in range(N):
    if T[i] == 'r':
        # 前回がpでは無かった時
        if i < K or T_list[i - K] != 'p':
            ans += P
            T_list.append('p')

        # 前回がpだった時
        elif i != N-1:
            # 次がr, またはpの時は最善手はr
            if T[i + 1] == 'r' or T[i + 1] == 'p':
                T_list.append('r')
            # 次がsの時は最善手はs
            else:
                T_list.append('s')

    elif T[i] == 's':
        # 前回がrでは無かった時
        if i < K or T_list[i - K] != 'r':
            ans += R
            T_list.append('r')

        # 前回がrだった時
        elif i != N-1:
            # 次がr, またはsの時は最善手はs
            if T[i + 1] == 'r' or T[i + 1] == 's':
                T_list.append('s')
            # 次がpの時は最善手はp
            else:
                T_list.append('p')

    elif T[i] == 'p':
        # 前回がsでは無かった時
        if i < K or T_list[i - K] != 's':
            ans += S
            T_list.append('s')

        # 前回がsだった時
        elif i != N-1:
            # 次がs, またはpの時は最善手はp
            if T[i + 1] == 's' or T[i + 1] == 'p':
                T_list.append('p')
            # 次がrの時は最善手はr
            else:
                T_list.append('r')
'''


'''

for j in range(K):

    for i in N_list:
        if i % K == j:
            mod_N_list[j].append(N_list.pop(N_list.index(i)))

    # mod_N_list[j] = [i for i in range(N) if (i % K == j)]

    print(mod_N_list)

    for k in range(len(mod_N_list[j])):

        if T[mod_N_list[j][k]] == 'r':
            # 前回がpでは無かった時
            if k == 0 or T_list[j][k - 1] != 'p':
                ans += P
                T_list[j].append('p')
            # 前回がpだった時
            elif k != len(mod_N_list[j]) - 1:
                # 次がr, またはpの時は最善手はr
                if T[mod_N_list[j][k + 1]] == 'r' or T[mod_N_list[j][k + 1]] == 'p':
                    T_list[j].append('r')

                # 次がsの時は最善手はs
                else:
                    T_list[j].append('s')

        elif T[mod_N_list[j][k]] == 's':
            # 前回がrでは無かった時
            if k == 0 or T_list[j][k - 1] != 'r':
                ans += R
                T_list[j].append('r')
            # 前回がrだった時
            elif k != len(mod_N_list[j]) - 1:
                # 次がp, またはrの時は最善手はs
                if T[mod_N_list[j][k + 1]] == 'p' or T[mod_N_list[j][k + 1]] == 'r':
                    T_list[j].append('s')

                # 次がrの時は最善手はr
                else:
                    T_list[j].append('p')

        elif T[mod_N_list[j][k]] == 'p':
            # 前回がsでは無かった時
            if k == 0 or T_list[j][k - 1] != 's':
                ans += S
                T_list[j].append('s')
            # 前回がsだった時
            elif k != len(mod_N_list[j]) - 1:
                # 次がs, またはpの時は最善手はp
                if T[mod_N_list[j][k + 1]] == 's' or T[mod_N_list[j][k + 1]] == 'p':
                    T_list[j].append('p')

                # 次がrの時は最善手はr
                else:
                    T_list[j].append('r')
'''

