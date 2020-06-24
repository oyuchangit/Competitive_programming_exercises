N, M = map(int, input().split())

ans = [-1] * N

flg = False

for m in range(M):
    s, c = input().split()
    s = int(s)

    if ans[s-1] != c and ans[s-1] != -1:
        flg = True
    
    elif s == 1 and c == '0':
        flg = True

    else:
        ans[s-1] = c

if flg:
    print(-1)
    exit()

ans_str = ''
for i in range(N):
    if i == 0 and ans[0] == -1:
        ans_str = '1'

    elif ans[i] == -1:
        ans_str = ans_str + '0'

    else:
        ans_str = ans_str + ans[i]

ans_str = int(ans_str)

if ans_str == 0:
    print(-1)
    exit()

print(ans_str)



# 未完
