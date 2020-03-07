# https://atcoder.jp/contests/abc046/tasks/abc046_b

N, K = map(int, input().split())

ans = ((K - 1) ** (N - 1)) * (K)
print(ans)