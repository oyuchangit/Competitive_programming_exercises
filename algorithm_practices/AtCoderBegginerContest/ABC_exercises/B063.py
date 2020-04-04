# https://atcoder.jp/contests/abc063/tasks/abc063_b

S = input()

S_set = set()
for i in range(len(S)):
    S_set.add(S[i])

if len(S_set) == len(S):
    print('yes')

else:
    print('no')

# 集合