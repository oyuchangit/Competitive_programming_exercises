# https://atcoder.jp/contests/abc157/tasks/abc157_b

A_list = [[] for _ in range(3)]

for i in range(3):
    A1, A2, A3 = map(int, input().split())
    A_list[i] += [A1, A2, A3]

N = int(input())

set1 = {A_list[0][0], A_list[0][1], A_list[0][2]}
set2 = {A_list[1][0], A_list[1][1], A_list[1][2]}
set3 = {A_list[2][0], A_list[2][1], A_list[2][2]}
set4 = {A_list[0][0], A_list[1][0], A_list[2][0]}
set5 = {A_list[0][1], A_list[1][1], A_list[2][1]}
set6 = {A_list[0][2], A_list[1][2], A_list[2][2]}
set7 = {A_list[0][0], A_list[1][1], A_list[2][2]}
set8 = {A_list[0][2], A_list[1][1], A_list[2][0]}


b_set = set()

for n in range(N):
    b = int(input())
    b_set.add(b)

if (set1 <= b_set or 
    set2 <= b_set or
    set3 <= b_set or
    set4 <= b_set or
    set5 <= b_set or
    set6 <= b_set or
    set7 <= b_set or
    set8 <= b_set):

    print('Yes')
else:
    print('No')





