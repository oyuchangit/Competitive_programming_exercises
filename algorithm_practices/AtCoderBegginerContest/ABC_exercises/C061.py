# https://atcoder.jp/contests/abc061/tasks/abc061_c

# N回操作, K番目に大きい整数
N, K = map(int, input().split())


a_b_list = []
for i in range(N):
    # aをb個挿入する
    a, b = map(int, input().split())
    a_b_list.append([a, b])

a_b_list = sorted(a_b_list)

ans = 0
sum_elements = 0

for i in range(N):

    sum_elements += a_b_list[i][1]
    ans = a_b_list[i][0]
    
    if sum_elements >= K:
        print(ans)
        exit()

