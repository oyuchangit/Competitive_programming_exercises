# https://atcoder.jp/contests/abc102/tasks/abc102_b

N = input()
A_list = input().split()

# 問題文勘違いしちゃった＞＜
# A_list = [A[i: i + 1] for i in range(0, len(A), 1)]

# 以下同義
'''
A_list = []
for i in range(0, len(A), 1):
    A_list.append(int(A[i: i + 1]))
'''

A_list_int = list(map(int, A_list))

max = max(A_list_int)
min = min(A_list_int)

print(max - min)