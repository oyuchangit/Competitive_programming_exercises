# https://atcoder.jp/contests/abc085/tasks/abc085_c

# N枚、Y円
N, Y = map(int, input().split())

for i in range(N + 1):
    for j in range(N + 1):
        
        z = N - (i + j)

        if z < 0:
            continue

        total = i*1000 + j*5000 + z*10000
        
        if total == Y:
            print(z, j, i)
            exit()

print('-1 -1 -1')






    # ダメな例
    # def dfs(total, c_1000, c_5000, c_10000, count_bill):

    #     if count_bill == N and total == Y:
    #         print(c_1000, c_5000, c_10000)
    #         exit()

    #     elif count_bill == N:
    #         return


    #     dfs(total + 1000, c_1000+1, c_5000, c_10000, count_bill+1)

    #     dfs(total + 5000, c_1000, c_5000+1, c_10000, count_bill+1)

    #     dfs(total + 10000, c_1000, c_5000, c_10000+1, count_bill+1)

    # dfs(0, 0, 0, 0, 0)
    # print(-1, -1, -1)