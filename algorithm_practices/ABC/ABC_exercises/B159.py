# https://atcoder.jp/contests/abc159/tasks/abc159_b

S = input()
N = len(S)
S_2 = S[: int((N - 1) / 2)]
S_3 = S[int(((N + 3) / 2)) - 1: ]

if S == S[:: -1] and S_2 == S_2[:: -1] and S_3 == S_3[:: -1]:
    print('Yes')

else:
    print('No')
