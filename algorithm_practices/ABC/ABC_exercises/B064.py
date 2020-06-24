# https://atcoder.jp/contests/abc064/tasks/abc064_b

N = int(input())
a_list = list(map(int, input().split()))

d = max(a_list) - min(a_list)

print(d)