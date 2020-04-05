# https://atcoder.jp/contests/abc075/tasks/abc075_b

H, W = map(int, input().split())

S_list = []

for h in range(H):
    S = list(input())
    S_list.append(S)


check_list = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0,1], [1, -1], [1, 0], [1, 1]]

for i in range(H):
    for j in range(W):
        if S_list[i][j] == '.':
            count = 0
            for k in check_list:
                k_i = i - k[1]
                k_j = j - k[0]
                if k_i >= 0 and k_j >= 0 and k_i < H and k_j < W:
                    if S_list[k_i][k_j] == '#':
                        count += 1
            
            S_list[i][j] = str(count)

    print(''.join(S_list[i]))
         