N, A, B = map(int, input().split())

num = N // (A + B)

tmp = N - (A + B) * num
if tmp <= A:
    blue_num = tmp
    red_num = 0

else:
    blue_num = A

blue_num = blue_num + num*A
print(blue_num)