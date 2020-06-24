# https://atcoder.jp/contests/abc066/tasks/abc066_a

a, b, c = map(int, input().split())

list_ = [a, b, c]
list_ = sorted(list_)

print(list_[0] + list_[1])