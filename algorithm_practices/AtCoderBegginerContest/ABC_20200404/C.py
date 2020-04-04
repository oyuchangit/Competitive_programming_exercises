N, K = map(int, input().split())

x = N // K

y = N - x*K

ans_1 = y
ans_2 = abs(y-K)

if ans_1 <= ans_2:
    print(ans_1)
else:
    print(ans_2)