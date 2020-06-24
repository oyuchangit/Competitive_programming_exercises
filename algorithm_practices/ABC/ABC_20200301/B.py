import numpy as np

A_list = []

for i in range(3):
    a = list(map(int, input().split()))
    A_list.append(a)

N = int(input())
narray = np.zeros((3, 3), dtype=np.int)


for j in range(N):
    b = int(input())

    for n in range(3):
        for m in range(3): 
            if A_list[n][m] == b:
                narray[n, m] = 1


n_list = np.count_nonzero(narray == 1, axis = 0)
m_list = np.count_nonzero(narray == 1, axis = 1)

print(narray)
print(n_list)
print(m_list)

if np.any(n_list == 3) or np.any(m_list == 3):
    print('Yes')
    exit()

if narray[0, 0] == 1 and narray[1, 1] == 1 and narray[2, 2] == 1:
    print('Yes')
    exit()

if narray[0, 2] == 1 and narray[1, 1] == 1 and narray[2, 0] == 1:
    print('Yes')
    exit()

print('No')

# 未完