# https://atcoder.jp/contests/abc054/tasks/abc054_b

N, M = map(int, input().split())
A_list = []
for n in range(N):
    a = input()
    A_list.append(a)

B_list = []
for m in range(M):
    b = input()
    B_list.append(b)

diff = N - m

for i in range(diff):
    is_same = False
    for j in range(diff):
        for b in range(M):
            if B_list[b] == A_list[i + b][j: j + M]:
                is_same = True
            else:
                is_same = False
                break

        if is_same:
            print('Yes')
            exit()

print('No')


# 5 3
# ..#..
# ..#.#
# .....
# #..#.
# .....
# ...
# ..#
# #.#
