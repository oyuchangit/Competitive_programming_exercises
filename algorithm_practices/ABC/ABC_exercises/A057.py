# https://atcoder.jp/contests/abc057/tasks/abc057_a

A, B = map(int, input().split())

start = A + B

if start >= 24:
    start -= 24

print(start)
