# https://atcoder.jp/contests/abc090/tasks/abc090_b

A, B = map(int, input().split())
count_target = 0

for i in range(A, B+1):
    str_i = str(i)
    reversed_i = str_i[::-1]

    if str_i == reversed_i:
        count_target += 1

print(count_target)






'''
A, B = map(int, input().split())
count_target = 0
for i in range(A, B + 1):
    str_i = str(i)
    reversed_i = ''
    for n_th_i in reversed(range(len(str_i))):
        reversed_i += str_i[n_th_i]

    if str_i == reversed_i:
        count_target += 1

print(count_target)
'''