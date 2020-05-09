# https://atcoder.jp/contests/abc145/tasks/abc145_c
import math
import copy

N = int(input())
x_y_list = []

for n in range(N):
    x, y = map(int, input().split())
    x_y_list.append([x, y])


visited = [False] * N
d_list = []
log_list = []

def dfs(distance, ex_coord, log):

    if all(visited):
        d_list.append(distance)
        log_list.append(copy.copy(log))

        return

    for i in range(N):
        if visited[i]:
            continue
        else:
            tmp = 0
            if ex_coord != []:
                tmp = (ex_coord[0] - x_y_list[i][0]) ** 2 + (ex_coord[1] - x_y_list[i][1]) ** 2
                tmp = math.sqrt(tmp)
                distance += tmp

            visited[i] = True
            log.append(i + 1)
            dfs(distance, x_y_list[i], log)
            del log[-1]
            visited[i] = False
            distance -= tmp

log_tmp = []
dfs(0, [], log_tmp)
print(sum(d_list) / len(d_list))

