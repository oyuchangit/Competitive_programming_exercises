N = int(input())
A_list = list(map(int, input().split()))


for a in A_list:
    if a % 2 == 0 and a % 3 != 0 and a % 5 != 0:
        print('DENIED')
        exit()

print('APPROVED')
