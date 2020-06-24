# https://atcoder.jp/contests/abc088/tasks/abc088_c

c_list = []

for i in range(3):
    c = list(map(int, input().split()))
    c_list.append(c)
    
a_list = [[] for i in range(3)]
b_list = [[] for i in range(3)]

a_list[0] = 0
b_list[0] = c_list[0][0]

a_list[1] = c_list[0][1] - b_list[0]
a_list[2] = c_list[0][2] - b_list[0]

b_list[1] = c_list[1][0] - a_list[0]
b_list[2] = c_list[2][0] - a_list[0]

if (
    ((a_list[1] + b_list[1]) == c_list[1][1])
    and ((a_list[2] + b_list[1]) == c_list[1][2])
    and ((a_list[1] + b_list[2]) == c_list[2][1])
    and ((a_list[2] + b_list[2]) == c_list[2][2])
    ):
    print('Yes')

else:
    print('No')    

