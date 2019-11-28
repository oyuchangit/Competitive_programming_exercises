N = int(input())
S = input()

half_N = int(N / 2)
if N % 2 == 0 and N != 2 and S[0:half_N] == S[half_N:len(S)]:
    print('Yes')

elif N == 2 and S[0] == S[1]:
    print('Yes')

else:
    print('No')


