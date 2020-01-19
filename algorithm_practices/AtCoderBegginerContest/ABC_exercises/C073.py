# https://atcoder.jp/contests/abc073/tasks/abc073_c
import sys
input = sys.stdin.readline

N = int(input())

# 集合　listよりも 検索などが高速　100倍ぐらい違うらしい
# 重複なしの順序も無し
ans_set = set()

for i in range(N):
    A = int(input())
    if A in ans_set:
        ans_set.remove(A)
    else:
        ans_set.add(A)

print(len(ans_set))