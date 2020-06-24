# https://atcoder.jp/contests/abc136/tasks/abc136_b

N = input()
len_n = len(N)
N = int(N)

count = 0

if len_n % 2 == 1:
    current_len_min_val = 10 ** (len_n - 1)
    count += N - current_len_min_val + 1

for i in range(1, len_n, 2):
    count += 10 ** i - 10 ** (i-1)


print(count)


# 1 <= N <= 10**5 なんだから、ループでぜんぶ調べればよかったな！馬鹿すぎ！