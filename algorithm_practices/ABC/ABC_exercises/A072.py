# https://atcoder.jp/contests/abc072/tasks/abc072_a

X, t = map(int, input().split())

diff = X - t

if diff < 0:
    print(0)
else:
    print(diff)