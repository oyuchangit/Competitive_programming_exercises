# https://atcoder.jp/contests/abc142/tasks/abc142_c

N = int(input())
A_list = list(map(int, input().split()))

# ans = str(A_list.index(1) + 1)
# for i in range(2, N + 1):
#     tmp = str(A_list.index(i) + 1)
#     ans = ' '.join([ans, tmp])



ans_list = [0] * N

for i in range(N):
    ans_list[A_list[i] - 1] = i + 1

# リストを空白区切りで出力
print(*ans_list)