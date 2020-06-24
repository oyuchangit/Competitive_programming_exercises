import copy

N, M, Q = map(int, input().split())
abcd_list = []

for q in range(Q):
    a, b, c, d = map(int, input().split())
    abcd_list.append([a, b, c, d])


A_list =[-1] * N
sum_max = 0

A_list_list =[]

def dfs(curr, count):
    if count >= N:
        sum_ = 0
        
        for q in range(Q):
            ai = abcd_list[q][0]
            bi = abcd_list[q][1]
            ci = abcd_list[q][2]
            di = abcd_list[q][3]

            if A_list[bi - 1] - A_list[ai - 1] == ci:
                sum_ += di
        global sum_max
        if sum_max <= sum_:
            sum_max = sum_

        A_list_list.append(copy.copy(A_list))

        return

    # 次の値を求める
    for i in range(curr, M + 1):
        A_list[count] = i
        dfs(i, count + 1)

dfs(1, 0)
print(sum_max)