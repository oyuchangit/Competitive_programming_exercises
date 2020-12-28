# https://atcoder.jp/contests/abc168/tasks/abc168_a

N = int(input())

last_num = int(str(N)[-1])

if last_num in {2, 4, 5, 7, 9}:
    print('hon')

elif last_num in {0, 1, 6, 8}:
    print('pon')

else:
    print('bon')