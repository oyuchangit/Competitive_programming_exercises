# https://atcoder.jp/contests/abc172/tasks/abc172_b

S = list(input())
T = list(input())
length = len(S)

ans = 0

for i in range(length):

    if S[i] != T[i]:
        ans += 1

print(ans)