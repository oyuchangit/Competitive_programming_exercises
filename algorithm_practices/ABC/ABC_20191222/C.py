import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

A, B = map(int, input().split())

# Aの倍数を1倍からB倍まで列挙して、それがBの倍数であるものを選ぶ
for b in range(1, B + 1):
    A_x = b * A
    if A_x % B == 0:
        print(A_x)
        exit()