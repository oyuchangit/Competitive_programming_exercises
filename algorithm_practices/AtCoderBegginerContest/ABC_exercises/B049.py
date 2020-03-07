# https://atcoder.jp/contests/abc049/tasks/abc049_b

H, W = map(int, input().split())

pic = []

for i in range(H):
    row = input()
    pic.append(row)

for i in range(H):
    for j in range(2):
        print(pic[i])