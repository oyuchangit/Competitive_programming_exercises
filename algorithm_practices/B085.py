# https://atcoder.jp/contests/abc085/tasks/abc085_b

N = int(input())
d_list = []

for d in range(N):
    d = int(input())
    d_list.append(d)

d_list.sort()
tmp_d = -1
mochi_count = 0
for i in range(N):
    if tmp_d == d_list[i]:
        continue
    else:
        tmp_d = d_list[i]
        mochi_count += 1

print(mochi_count)