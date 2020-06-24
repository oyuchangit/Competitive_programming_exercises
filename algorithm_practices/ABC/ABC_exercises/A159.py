# https://atcoder.jp/contests/abc159/tasks/abc159_a

N, M = map(int, input().split())

# 奇数同士の数
odd_odd = M * (M - 1) / 2

# 偶数同士の数
even_even = N * (N - 1) / 2

print(int(even_even + odd_odd))