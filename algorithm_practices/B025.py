# https://atcoder.jp/contests/agc025/tasks/agc025_a

# 各位の和を求める
def sum_each_digit(n):
    total_each_digit = 0
    while n > 0:
        total_each_digit += n % 10
        n //= 10
    return total_each_digit


N = int(input())
min_AandB = -1

for A in range(1, N):
    B = N - A

    A_digit = sum_each_digit(A)
    B_digit = sum_each_digit(B)
    sum_digit = A_digit + B_digit

    if sum_digit < min_AandB or min_AandB < 0:
        min_AandB = sum_digit

print(sum_digit)