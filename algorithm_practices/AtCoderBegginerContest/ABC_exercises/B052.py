# https://atcoder.jp/contests/abc052/tasks/abc052_b

N = int(input())
S = input()

max_count = 0
curr_count = 0

for s in S:
    if s == 'I':
        curr_count += 1

    elif s == 'D':
        curr_count -= 1

    if curr_count > max_count:
        max_count = curr_count

print(max_count)