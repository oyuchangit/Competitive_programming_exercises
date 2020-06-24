N, K= map(int, input().split())

p_list = list(map(int, input().split()))

# 累積和初期化
s_list = [0] * (N + 1)

for i in range(N):
	s_list[i + 1] = s_list[i] + p_list[i]

# 隣り合うK個の要素の和が最大になるような範囲の開始位置を求める
max_s_sum = 0
max_sum_index = 0

for n in range(N - K + 1):
    s_sum = s_list[n + K] - s_list[n]
    if max_s_sum < s_sum:
        max_s_sum = s_sum
        max_sum_index = n

# 求めた開始位置から隣接するK個の要素の期待値を求める
ans = 0
for k in range(K):
    x = p_list[max_sum_index]
    ans += (x + 1) / 2
    max_sum_index += 1
  
print(ans)