# https://atcoder.jp/contests/abc088/tasks/abc088_b

N = int(input())

a_list = list(map(int, input().split()))
a_list.sort(reverse = True)

count = 0
allice_total = 0
bob_total = 0
for a in a_list:
    if count % 2 == 0:
        allice_total += a
    else:
        bob_total += a
    count += 1

print(allice_total - bob_total)



