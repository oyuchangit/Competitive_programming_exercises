# https://atcoder.jp/contests/abc053/tasks/abc053_b
s = input()
length = range(0, len(s))
first_A = -1

for i in length:
    if s[i] == 'A':
        first_A = i
        break
    else:
        continue

last_Z = -1

for j in list(reversed(length)):
    if s[j] == 'Z':
        last_Z = j
        break
    else:
        continue

max_diff = last_Z - first_A
print(max_diff + 1)
