# N科目, K点満点, 平均M点以上
N, K, M = map(int, input().split())

A_list = list(map(int, input().split()))
sum_A = sum(A_list)

ans_A = N * M - sum_A

if 0 <= ans_A <= K:
    print(ans_A)
elif ans_A <= 0:
    print(0)
else:
    print(-1)