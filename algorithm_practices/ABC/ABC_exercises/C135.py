# https://atcoder.jp/contests/abc135/tasks/abc135_c

N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

count_defeat = 0

for i, b in enumerate(B_list):
    if A_list[i] >= b:
        count_defeat += b

    else:
        count_defeat += A_list[i]
        remain_b = (b - A_list[i])

        if remain_b > A_list[i + 1]:
            count_defeat += A_list[i + 1]
            A_list[i + 1] = 0

        else:
            count_defeat += remain_b
            A_list[i + 1] -= remain_b

print(count_defeat)
