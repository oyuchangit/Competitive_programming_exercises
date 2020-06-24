# https://atcoder.jp/contests/abc143/tasks/abc143_b

N = int(input())
d_list = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        ans += d_list[i] * d_list[j]

print(ans)