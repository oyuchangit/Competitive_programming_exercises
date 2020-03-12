import math

A, B = map(int, input().split())

ans_A = A * (100 / 8)
ans_B = B * 10

for x in range(1251):
    if math.floor(x * 0.08) == A and math.floor(x * 0.1) == B:
        print(x)
        exit()

print(-1)