# https://atcoder.jp/contests/abc084/tasks/abc084_c

N = int(input())
C_list = []
S_list = []
F_list = []

for n in range(N - 1):
    C, S, F = map(int, input().split())
    C_list.append(C)
    S_list.append(S)
    F_list.append(F)


for i in range(N - 1):

    t = 0
    for j in range(i, N - 1):
        
        # 時刻tにj番目の駅にいる
        # t <= Sなら時刻Sにjを出発して、S + C秒で次の駅に到着する
        if t <= S[j]:
            t = S[j] + C[j]
        
        # そうではなく、t % F == 0なら時刻tにjを出発する
        elif t % F[j] == 0:
            t += C[j]

        else:
            t += 