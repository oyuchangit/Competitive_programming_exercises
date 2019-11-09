# https://atcoder.jp/contests/abc042/tasks/abc042_b

N, L = map(int, input().split())
S_list = []
for s in range(N):
    s = input()
    S_list.append(s)

S_list.sort()
combined_S = ''
for i in range(N):
    combined_S += S_list[i]

print(combined_S)
