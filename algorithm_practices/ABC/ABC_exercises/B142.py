# https://atcoder.jp/contests/abc142/tasks/abc142_b

N, K = map(int, input().split())
h_list = list(map(int, input().split()))

count = 0

for i in h_list:
    if i >= K:
        count += 1

print(count)