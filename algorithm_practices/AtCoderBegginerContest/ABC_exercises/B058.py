# https://atcoder.jp/contests/abc058/tasks/abc058_b

O = input()
E = input()

len_E = len(E)
len_O = len(O)

E_count = 0
O_count = 0

total_len = len_E + len_O

ans = ''

for t in range(1, total_len + 1):
    if t % 2 == 0:
        ans = ans + E[E_count]
        E_count += 1
    else:
        ans = ans + O[O_count]
        O_count += 1

print(ans)