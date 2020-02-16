N = int(input())
A_list = list(map(int, input().split()))
A_list_len = len(A_list)

A_set = set(A_list)
A_set_len = len(A_set)

if int(A_list_len) == int(A_set_len):
    print('YES')
else:
    print('NO')