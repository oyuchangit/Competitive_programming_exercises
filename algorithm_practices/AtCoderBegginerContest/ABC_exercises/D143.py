# https://atcoder.jp/contests/abc143/tasks/abc143_d

import bisect

N = int(input())
L_list = list(map(int, input().split()))
L_list = sorted(L_list)
count = 0

for a in range(N-2):
    for b in range(a + 1, N-1):
        c_min = L_list[b + 1]
        c_max = L_list[a] + L_list[b]
        c_max_idx = bisect.bisect_left(L_list, c_max)
        c_count = c_max_idx - (b + 1)
        count += c_count

print(count)