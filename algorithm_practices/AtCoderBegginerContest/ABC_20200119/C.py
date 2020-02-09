N = int(input())
p_list = list(map(int, input().split()))


i_list = [False] * N

min_tmp = p_list[0]

for i in range(N):
    if p_list[i] > min_tmp:
        i_list[i] = False

    else:
        min_tmp = p_list[i]
        i_list[i] = True


ans = i_list.count(True)
print(ans)





# def dfs(i):

#     if 


#     for j in range(N):
#         p_j = p_list[j]
#         p_i = p_list[i]

#         if p_j < p_i:
#             return
#         else:
#             dfs(i)




