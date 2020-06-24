# https://atcoder.jp/contests/abc135/tasks/abc135_a

A, B = map(int, input().split())


K = (A + B) / 2

if (A + B) % 2 == 0:
    print(int(K))

else:
    print('IMPOSSIBLE')
