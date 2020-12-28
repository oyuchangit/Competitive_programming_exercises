N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b = [0], [0]
for i in range(N):
    a.append(a[i] + A[i])
    
for i in range(M):
    b.append(b[i] + B[i])
    ans, j = 0, M

for i in range(N + 1):
    if a[i] > K:
        break
    while b[j] > K - a[i]:
        j -= 1
    ans = max(ans, i + j)
print(ans)





















# # https://atcoder.jp/contests/abc172/tasks/abc172_c

# N, M, K = map(int, input().split())
# A_list = list(map(int, input().split()))
# B_list = list(map(int, input().split()))


# curr_A = 0
# curr_B = 0
# total_t = 0
# count_r = 0

# len_A = len(A_list)
# len_B = len(B_list)

# while curr_A < len_A or curr_B < len_B:
#     if curr_A >= len_A:
#         total_t += B_list[curr_B]
#         curr_B += 1
    
#     elif curr_B >= len_B:
#         total_t += A_list[curr_A]
#         curr_A += 1

#     elif A_list[curr_A] <= B_list[curr_B]:
#         total_t += A_list[curr_A]
#         curr_A += 1
    
#     else:
#         total_t += B_list[curr_B]
#         curr_B += 1

#     count_r += 1
    
#     if total_t > K:
#         count_r -= 1
#         break


# print(count_r)


