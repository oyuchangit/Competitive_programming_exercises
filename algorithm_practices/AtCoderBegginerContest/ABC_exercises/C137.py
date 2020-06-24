# https://atcoder.jp/contests/abc137/tasks/abc137_c

import math

N = int(input())

s_dic = {}
s_set = set()

for i in range(N):
    s = input()

    s = ''.join(sorted(s))

    if s in s_set:
        s_dic[s] += 1

    else:
        s_set.add(s)
        s_dic[s] = 1


result = 0

for val in s_dic.values():

    if val > 1:
        result += int((val * (val - 1)) / 2)

print(result)






