# https://atcoder.jp/contests/abc095/tasks/abc095_b
N_X = input().split()
N = int(N_X[0])
X = int(N_X[1])

m = []
list_range = range(N)
total_m = 0
for i in list_range:
    m.append(int(input()))
    total_m += m[i]

remaining_m = X - total_m


min_m = min(m)
index_min_m = m.index(min_m)
additional_pieces = remaining_m // min_m
total_pieces = additional_pieces + N
print(total_pieces)




