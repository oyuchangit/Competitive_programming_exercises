N, M = map(int, input().split())
H_list = list(map(int, input().split()))

good_list = [True] * N

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1

    if H_list[A] > H_list[B]:
        good_list[B] = False
    elif H_list[A] < H_list[B]:
        good_list[A] = False
    elif H_list[A] == H_list[B]:
        good_list[A] = False
        good_list[B] = False

ans = good_list.count(True)
print(ans)





# import sys
# sys.setrecursionlimit(100000000)

# N, M = map(int, input().split())
# H_list = list(map(int, input().split()))
# road_list = []


# graph_list = [[] for i in range(N)]

# for m in range(M):
#     A, B = map(int, input().split())
#     road_list.append([A, B])

#     A -= 1
#     B -= 1

#     graph_list[A].append(B)
#     graph_list[B].append(A)

# visited = [False] * N
# visited[0] = True
# LorS_list = [0] * N

# def dfs(current, graph_list):

#     global LorS_list
#     global visited

#     if len(graph_list[current]) == 0:
#         LorS_list[current] = 2

#     for i in graph_list[current]:
#         if visited[i] == False:
#             visited[i] = True


#             if H_list[current] > H_list[i] and LorS_list[current] != 1:
#                 LorS_list[current] = 2
#                 LorS_list[i] = 1

#             elif H_list[current] < H_list[i] and LorS_list[i] != 1:
#                 LorS_list[current] = 1
#                 LorS_list[i] = 2

#             elif H_list[current] == H_list[i]:
#                 LorS_list[current] = 1
#                 LorS_list[i] = 1

#             dfs(i, graph_list)


# start = 0
# while all(visited) == False:
#     visited[start] = True
#     dfs(start, graph_list)

#     if False in visited:
#         start = visited.index(False)



# ans = LorS_list.count(2)

# print(ans)