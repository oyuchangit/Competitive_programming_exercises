# https://atcoder.jp/contests/abc136/tasks/abc136_c

N = int(input())
H_list = list(map(int, input().split()))

past_H = 0
can_substract = False

for i in range(1, N - 1):

    if H_list[i] - H_list[i + 1] > 1:
        print('No')
        exit()

    if (H_list[i] - H_list[i + 1] == 1) and (H_list[i] - H_list[i - 1] < 1):
        print('No')
        exit()

    if H_list[i] - H_list[i - 1] >= 1:
        H_list[i] -= 1
        continue

print('Yes')

    
