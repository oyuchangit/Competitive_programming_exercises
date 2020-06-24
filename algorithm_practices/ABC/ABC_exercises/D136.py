# # https://atcoder.jp/contests/abc136/tasks/abc136_d

# 馬鹿の回答　解けない

# S = input()
# N = len(S)

# switchPoint_list = [0] * N

# def add_children(i, current_even_count, current_odd_count, switchPoint_list):
#     # 集計作業
#     # 切り替わったポイントから偶数距離離れている点の子供は偶数回目の施行で
#     # 切り替わったポイントに戻ってくる
#     if (i+1) % 2 == 0:
#         switchPoint_list[i] += current_even_count
#         switchPoint_list[i-1] += current_odd_count

#     else:
#         switchPoint_list[i] += current_odd_count
#         switchPoint_list[i-1] += current_even_count

#     return switchPoint_list


# current_odd_count = 0
# current_even_count = 0

# current_LR = 'R'
# past_i = 0

# for i in range(N):
    
#     if (i + 1) % 2 == 0:
#         current_even_count += 1

#     else:
#         current_odd_count += 1


#     if S[i] != current_LR and S[i] == 'L':
#         switchPoint_list = add_children(i, current_even_count, current_odd_count, switchPoint_list)

#         current_LR = 'L'
#         past_i = i
#         current_odd_count = 0
#         current_even_count = 0


#     elif S[i] != current_LR and S[i] == 'R':
#         switchPoint_list = add_children(past_i, current_odd_count, current_even_count, switchPoint_list)
#         current_LR = 'R'
#         current_odd_count = 0
#         current_even_count = 0


# print(*switchPoint_list)




# 賢者の回答

S = input()
N = len(S)

ans = [1]*N


# 左から1ずつカウントしていって、Rの時のことだけ考える
for i,s in enumerate(S):
    if s=="R":
        s2 = S[i+1]
        if s2 == "R":
            ans[i+2] += ans[i]
            ans[i] = 0


# 右から1ずつカウントしていって、Lの時のことだけ考える
for i in range(N-1,-1,-1):
    s = S[i]
    if s=="L":
        s2 = S[i-1]
        if s2 == "L":
            ans[i-2] += ans[i]
            ans[i] = 0

print(*ans)
