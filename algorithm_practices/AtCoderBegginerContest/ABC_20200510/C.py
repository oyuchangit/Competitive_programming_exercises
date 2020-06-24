import numpy as np

N, M, X = map(int, input().split())

# 参考書の値段
C_list = []

# 参考書が持つ理解度を上げる能力
A_list = []

for i in range(N):
    C_A_list = list(map(int, input().split()))
    C_list.append(C_A_list[0])
    A_list.append(C_A_list[1:])

A_list = np.array(A_list)

is_use_list = [False] * N

min_value = -1
understand_list = [0] * M
understand_list = np.array(understand_list)
c_total = 0

def dfs(i):

    global c_total
    global understand_list
        
        
    if min(understand_list) >= X:

        global min_value
        if min_value == -1 or c_total < min_value:
            min_value = c_total

    if i >= N:
        return


    is_use_list[i] = True
    understand_list = understand_list + A_list[i]
    c_total += C_list[i]
    dfs(i + 1)
    is_use_list[i] = False
    understand_list = understand_list - A_list[i]
    c_total -= C_list[i]
    dfs(i + 1)

dfs(0)

print(min_value)