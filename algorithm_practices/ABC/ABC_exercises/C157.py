# https://atcoder.jp/contests/abc157/tasks/abc157_c

N, M = map(int, input().split())
N_list = [0] * N
N_set_list = [False] * N

for i in range(M):
    s, c = map(int, input().split())
    s -= 1
  
    if s > N -1 or (s == 0 and c == 0 and N != 1):
        print(-1)
        exit()

    elif N_set_list[s] and (N_list[s] != c):
        print(-1)
        exit()

    else:
        N_list[s] = c
        N_set_list[s] = True

if N_list[0] == 0 and N != 1:
    N_list[0] = 1

print(''.join(map(str, N_list)))
