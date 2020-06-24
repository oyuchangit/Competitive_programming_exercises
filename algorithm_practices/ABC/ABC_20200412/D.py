N = int(input())
S = input()

r = S.count('R')
g = S.count('G')
b = S.count('B')

ans = 0

# 1つ目の条件を満たす組の総数は
all_1 = r * g * b

# 1つ目の条件を満たすかつ2つ目の条件を満たさない組の個数
for i in range(N):
    for j in range(i + 1, N):
        k = 2*j - i
        if k >= N:
            continue
        if (S[i] is not S[j]) and (S[i] is not S[k]) and (S[j] is not S[k]):
            ans += 1

s = all_1 - ans

print(s)


# N = int(input())
# S = input()

# ans = 0
# k = 0
# for i in range(N):
#     for j in range(N):
#         k = 2*j - i

#         if (S[i] is not S[j]) and (S[i] is not S[k]) and (S[j] is not S[k]):
#             ans += 1