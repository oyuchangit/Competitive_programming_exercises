X = int(input())

is_prime_num_list = [True] * 100005
is_prime_num_list[0] = False
is_prime_num_list[1] = False

for i in range(2, X + 1):
    if is_prime_num_list[i] == True:

        # iの倍数番目をFalseにする
        for j in range(2 * i, 100005, i):
            is_prime_num_list[j] = False

prime_num_list = [i for i, j in enumerate(is_prime_num_list) if i >= X and j == True]

print(min(prime_num_list))


'''
if is_prime_num_list[X] == True:
    print(X)
    exit()
''' 

'''
while True:
    X += 1
    is_target = True
    for i in prime_num_list:
        if X % i == 0:
            is_target = False
            break

    if is_target:
        print(X)
        exit()
'''
    
    




        





