H, N = map(int, input().split())
A_list = list(map(int, input().split()))
total = 0
for A in A_list:
    total += A

if total >= H:
    print('Yes')
else:
    print('No')