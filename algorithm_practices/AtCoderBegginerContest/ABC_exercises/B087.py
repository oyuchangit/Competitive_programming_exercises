# https://atcoder.jp/contests/abc087/tasks/abc087_b

A_having = int(input())
B_having = int(input())
C_having = int(input())
X = int(input())

patterns = 0
for a in range(A_having + 1):
    for b in range(B_having + 1):
        for c in range(C_having + 1):
            total = a * 500 + b * 100 + c * 50
            if total == X:
                patterns += 1

print(patterns)
