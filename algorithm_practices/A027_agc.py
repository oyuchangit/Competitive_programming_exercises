# https://atcoder.jp/contests/agc027/tasks/agc027_a

N, x = map(int, input().split())
a_list = list(map(int, input().split()))
a_list.sort()

tmp_total_a = 0
count_happy = 0
for a in a_list:
    tmp_total_a += a
    if tmp_total_a <= x:
        count_happy += 1
    else:
        break

if tmp_total_a < x:
    count_happy -= 1
    
print(count_happy)
