# https://atcoder.jp/contests/abc063/tasks/abc063_a

A, B = map(int, input().split())

total = A + B

if total >= 10:
    print('error')

else:
    print(total)