K = int(input())
A, B = map(int, input().split())

a = B // K
if a*K >= A:
    print('OK')

else:
    print('NG')

