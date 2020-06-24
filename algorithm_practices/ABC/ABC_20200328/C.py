# 湖の円周、家の数
K, N = map(int, input().split())

A_list = list(map(int, input().split()))

A_list = sorted(A_list)

max_d = 0

for i in range(N-1):
    d = A_list[i + 1] - A_list[i]

    if d > max_d:
        max_d = d

l = K - A_list[N -1] + A_list[0]
if l > max_d:
    max_d = l

print(K - max_d)

