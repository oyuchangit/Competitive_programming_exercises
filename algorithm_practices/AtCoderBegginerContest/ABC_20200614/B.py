X, Y = map(int, input().split())


A = 2 * X - (Y / 2)

if A.is_integer() and (A >= 0) and (X - A) >= 0:
    print('Yes')

else:
    print('No')
