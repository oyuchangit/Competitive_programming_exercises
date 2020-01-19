# N問出題, M回提出
N, M = map(int, input().split())

p_S_list = []

WA = 'WA'
AC = 'AC'

question_list = [False] * N
WA_count_list = [0] * N

count_AC = 0
count_WA = 0

for i in range(M):
    p, S = input().split()
    int_p = int(p)
    
    if S == WA and question_list[int_p - 1] == False:
        WA_count_list[int_p - 1] += 1

    if S == AC and question_list[int_p - 1] == False:
        count_AC += 1
        count_WA += WA_count_list[int_p - 1]
        question_list[int_p - 1] = True

print(str(count_AC) + ' ' + str(count_WA))








'''
first_AC_index_list = []
AC_set = set([])

for j in range(M):
    p, S = input().split()
    int_p = int(p)
    p_S_list.append([int_p, S])

    if S == AC and (int_p not in AC_set):
        first_AC_index_list.append([j, int_p])
        AC_set.add(int_p)

count_AC = len(first_AC_index_list)
count_WA = 0
# for i in range(1, N + 1):
#     # i問目の問題について考える
#     if [i, AC] in p_S_list:
#         count_AC += 1

#         first_AC_index = p_S_list.index([i, AC])

#         count_WA += p_S_list[:first_AC_index].count([i, WA])

for i_list in first_AC_index_list:
    count_WA += p_S_list[:i_list[0]].count([i_list[1], WA])

ans = str(count_AC) + ' ' + str(count_WA)

print(ans)

'''


