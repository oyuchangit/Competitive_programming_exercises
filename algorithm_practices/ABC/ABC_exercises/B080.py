# https://atcoder.jp/contests/abc080/tasks/abc080_b

N = int(input())

# 各位の値を足し算する処理
def sum_each_digit(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


if N % sum_each_digit(N) == 0:
    result = 'Yes'
else:
    result = 'No'

print(result)
