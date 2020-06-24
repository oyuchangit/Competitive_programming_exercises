# https://atcoder.jp/contests/abc134/tasks/abc134_c

N = int(input())

max_a = 0
max_i = 0
max_a_2 = 0

for i in range(N):
    A = int(input())
    
    if A >= max_a:
        max_a_2 = max_a
        max_a = A
        max_i = i

    elif A >= max_a_2:
        max_a_2 = A

for i in range(N):
    if i != max_i:
        print(max_a)

    else:
        print(max_a_2)


