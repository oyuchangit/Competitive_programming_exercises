import copy

# https://atcoder.jp/contests/abc050/tasks/abc050_b

N = int(input())
T_list = list(map(int, input().split()))
M = int(input())

P_list = []
X_list = []
for m in range(M):
    p, x = map(int, input().split())
    P_list.append(p)
    X_list.append(x)

for p in range(M):
    T_d_list = copy.copy(T_list)
    T_d_list[P_list[p] - 1] = X_list[p]

    print(sum(T_d_list))
