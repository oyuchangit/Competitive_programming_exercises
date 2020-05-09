# https://atcoder.jp/contests/abc159/tasks/abc159_d

N = int(input())
A_list = list(map(int, input().split()))

box = [0] * (N + 1)
box_2 = [0] * (N + 1)
box_3 = [0] * (N + 1)

for i in range(N):
    box[A_list[i]] += 1

for i in range(N + 1):
    if box[i] > 1:
        box_2[i] = (box[i] * (box[i] - 1)) / 2
        box_3[i] = ((box[i] - 1) * (box[i] - 2)) / 2

ans_base = sum(box_2)

for i in range(N):

    if box[A_list[i]] > 0:
        diff = box_2[A_list[i]] - box_3[A_list[i]]
        print(int(ans_base - diff))
    else:
        print(int(ans_base))
    
