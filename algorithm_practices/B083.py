# https://atcoder.jp/contests/abc083/tasks/abc083_b

# 各位の値を足し算する処理2
def sum_each_digit(n):
    total_each_digit = 0
    while n > 0:
        total_each_digit += n % 10
        n //= 10
    return total_each_digit


N, A, B = map(int, input().split())
target_total = 0    # 加算対象の数値の和

for n in range(1, N + 1):

    if A <= sum_each_digit(n) <= B:
        target_total += n

print(target_total)



'''
N, A, B = map(int, input().split())

target_total = 0    # 加算対象の数値の和

for n in range(1, N + 1):
    total_each_digit = 0    # 各位の和      
    str_n = str(n)
    n_length = len(str_n)  # nの桁数
    
    for i in range(n_length):
        total_each_digit += int(str_n[i])

    if A <= total_each_digit <= B:
        target_total += n

print(target_total)
'''