A_1, A_2, A_3 = map(int, input().split())
ans = A_1 + A_2 + A_3

if ans >= 22:
    print('bust')
else:
    print('win')