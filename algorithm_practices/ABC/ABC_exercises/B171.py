# https://atcoder.jp/contests/abc171/tasks/abc171_b

N, K = map(int, input().split())
p_list = list(map(int, input().split()))

p_list = sorted(p_list)

total_val = 0

for i in range(K):
    total_val += p_list[i]

print(total_val)