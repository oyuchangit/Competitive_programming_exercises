# https://atcoder.jp/contests/abc146/tasks/abc146_b

N = int(input())
S = input()
max_val = ord('Z')
N_mod = N % 26

ans = ''

for i in range(len(S)):
    a = ord(S[i]) + N_mod
    if a > max_val:
        a = a - 26

    ans += chr(a)

print(ans)
