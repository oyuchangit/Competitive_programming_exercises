# https://atcoder.jp/contests/abc043/tasks/abc043_b

s = input()

ans = ''

for i in s:
    if i == 'B':
        len_ans = len(ans)
        ans = ans[0: len_ans-1]

    else:
        ans = ans + i

print(ans)
