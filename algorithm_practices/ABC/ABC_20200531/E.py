N = int(input())

# A <= X <= B

max_x = 0
min_x = 10 ** 9 + 1

for n in range(N):
    A, B = map(int, input().split())

    if A < min_x:
        min_x = A

    if B > max_x:
        max_x = B
    
    

