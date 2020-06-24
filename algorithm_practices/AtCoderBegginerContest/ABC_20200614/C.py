X, N = map(int, input().split())
p_list = list(map(int, input().split()))

if N == 0:
    print(X)
    exit()

p_set = set(p_list)
min_p = min(p_list)
max_p = max(p_list)

compare_X = X
min_d = 100000
min_d_i = compare_X

while True:
    if compare_X not in p_set:
        d = abs(X - compare_X)
        min_d = min(min_d, d)
        if min_d == d:
            min_d_i = compare_X

    if compare_X > max_p:
        break

    compare_X += 1

compare_X = X


while True:
    if compare_X not in p_set:
        d = abs(X - compare_X)
        min_d = min(min_d, d)
        if min_d == d:
            min_d_i = compare_X

    if compare_X < min_p:
        break

    compare_X -= 1


print(min_d_i)
        




