N = int(input())
A_list = list(map(int, input().split()))

ans = 1

p = 10 ** 18

for a in A_list:
    ans *= a
    if ans > p:
        ans = -1
        break

if 0 in A_list:
    print(0)
else:
    print(ans)

