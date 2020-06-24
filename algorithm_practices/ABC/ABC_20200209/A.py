S, T = input().split()
A, B = map(int, input().split())
U = input()

if S == U:
    ans = str(A-1) + ' ' + str(B)
else:
    ans = str(A) + ' ' + str(B-1)

print(ans)