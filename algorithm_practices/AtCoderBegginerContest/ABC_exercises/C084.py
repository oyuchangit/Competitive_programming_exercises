# https://atcoder.jp/contests/abc084/tasks/abc084_c

N = int(input())    # N個の駅
C_list = []         # 駅iからi+1に向かうまでにかかる時間
S_list = []         # 最初の列車が開通式開始後S秒後に駅iを出発
F_list = []         # F秒おきに発車

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
        if t <= S_list[j]:
            t = S_list[j] + C_list[j]
        
        # そうではなく、t % F == 0なら時刻tにjを出発する
        elif t % F_list[j] == 0:
            t += C_list[j]

        # そうでないなら、開通式開始 t + Fj − (t ％ Fj ) 秒後にjを出発する
        else:
            t += F_list[j] - (t % F_list[j]) + C_list[j]

    print(t)

print(0)