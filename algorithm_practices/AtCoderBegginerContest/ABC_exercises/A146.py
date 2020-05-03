# https://atcoder.jp/contests/abc146/tasks/abc146_a

S = input()
week_list =  ['SUN','MON','TUE','WED','THU','FRI','SAT']

S_week = week_list.index(S)

ans = 7 - S_week

print(ans)
