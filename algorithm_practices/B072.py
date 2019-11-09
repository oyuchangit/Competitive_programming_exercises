# https://atcoder.jp/contests/abc072/tasks/abc072_b

s = input()
list = range(0, len(s), 2)
s_result = ''
for i in list:
    s_result = s_result + s[i]

print(s_result)