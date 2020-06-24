import math

N = int(input())
P_list = list(map(int, input().split()))
Q_list = list(map(int, input().split()))
N_list = list(range(1, N + 1))

current_permutation = [0] * N
current_index = 0
A = 0
B = 0


def dfs(i, current_permutation):

    # 終了条件
    if i >= N:
        global current_index
        current_index += 1

        global A
        if current_permutation == P_list:
            A = current_index
            
        global B    
        if current_permutation == Q_list:
            B = current_index

        if A != 0 and B != 0:
            print(abs(A - B))
            exit()

        return

    for j in range(N):
        if (N_list[j] in current_permutation) == False:
            current_permutation[i] = N_list[j]
            dfs(i + 1, current_permutation)
            current_permutation[i] = 0


dfs(0, current_permutation)