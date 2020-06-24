ans = ''

for i in range(10 ** 5):

    ans = ans + str(i) + ' '

ans = ans + str(10 ** 5 + 1)



path_w = 'C:/Users\81905\work\python_works\algorithm_practices\test\outout.txt'

with open(path_w, mode='w') as f:
    f.write(ans)

with open(path_w) as f:
    print(f.read())


