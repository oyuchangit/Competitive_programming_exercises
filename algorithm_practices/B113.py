# https://atcoder.jp/contests/abc113/tasks/abc113_b

N = input()
T_A = input().split()
T = int(T_A[0])
A = int(T_A[1])
H_list = list(map(int, input().split()))

i = 1
i_H_list = []
for H in H_list:
    ave_T = T - H * 0.006
    i_H_list.append([i, abs(A - ave_T)])
    i += 1

min_diff = -1
min_diff_i = -1
for i in range(len(H_list)):
    if min_diff > i_H_list[i][1] or min_diff == -1:
        min_diff = i_H_list[i][1]
        min_diff_i = i_H_list[i][0]
print(min_diff_i)

# print(ave_T)