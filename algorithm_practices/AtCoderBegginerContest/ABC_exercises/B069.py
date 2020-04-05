# https://atcoder.jp/contests/abc069/tasks/abc069_b

s = input()

first_s = s[0]
last_s = s[-1]
middle_s = str(len(s) - 2)
ans = first_s + middle_s + last_s

print(ans)