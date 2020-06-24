A, B, C, K = map(int, input().split())

a_tmp = A - K
ans = 0


if a_tmp <= 0:
    ans += A
    
    b_tmp = B + a_tmp

    if b_tmp < 0:

        ans += b_tmp
        
else:
    ans += K


print(ans)