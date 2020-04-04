N, M = map(int, input().split())
A_list = list(map(int, input().split()))

A_list = sorted(A_list, reverse=True)

sum_A = sum(A_list)

if A_list[M-1] < (sum_A * (1 / (4 * M))):
    print('No')
else:
    print('Yes')