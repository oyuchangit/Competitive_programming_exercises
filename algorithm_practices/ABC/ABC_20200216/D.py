N, K = map(int, input().split())
A_list = list(map(int, input().split()))





# 未AC













# N, K = map(int, input().split())
# A_list = list(map(int, input().split()))

# A_list.sort()

# range_N_list = list(range(1, N + 1))
# range_N_list.reverse()

# s_list = [0] * (N + 1)

# for i in range(N):
#     s_list[i + 1] = s_list[i] + range_N_list[i]

#     if s_list[i + 1] > K:
#         index_left = i
#         hasuu = K - index_left
#         break


# # 一番小さい数字から数えて
# # index_left番目の数字 × index_left番目の数字から端数番目の数字
# num_index_left_1 = A_list[index_left]
# num_index_left_2 = A_list[index_left + hasuu]

# ans = num_index_left_1 * num_index_left_2

# print(ans)