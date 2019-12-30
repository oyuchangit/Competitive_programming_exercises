A, B, K = map(int, input().split())

if A >= K:
    print(str(A - K) + ' ' + str(B))

if A < K:
    ans = B - (K - A)
    if ans >= 0:
        print('0' + ' ' + str(ans))
    else:
        print('0 0')