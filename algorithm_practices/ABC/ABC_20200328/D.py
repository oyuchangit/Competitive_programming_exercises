N, X, Y = map(int, input().split())

ans = [0] * (N - 1)

for i in range(1, 1 + N):
    for j in range(i + 1, 1 + N):
        k = min(j - i, abs(X - i) + abs(Y - j) + 1)
        ans[k - 1] += 1

for a in ans:
    print(a)



# import copy

# N, X, Y = map(int, input().split())

# X -= 1
# Y -= 1

# graph = [[] for i in range(N)]

# for i in range(N):
#     if i != N-1:
#         graph[i + 1].append(i)

#     if i != 0:
#         graph[i].append(i + 1)

# graph[X].append(Y)
# graph[Y].append(X)

# INF = 10000
# min_graph = []

# for i in range(N):

#     if i != 0:
#         del graph[0]

#     graph_d = [INF] * (N - i)
#     graph_d[0] = 0

#     for j in range(N - i):
#         for k in graph[j]:
#             edge = [j, k]

#             if graph_d[edge[0]] != INF and graph_d[edge[1]] > graph_d[edge[0]] + 1:
#                 graph_d[edge[1]] = graph_d[edge[0]] + 1

#     copy_list = copy.copy(graph_d)
#     min_graph.append(copy_list)

# for k in range(1, N):
#     for x in range(N):
#         mi = min_graph[x]
#         mi_list = [i for i, x in enumerate(mi) if i == k]
        
#         for z in range(len(mi_list)):
#             print(x, z + x)
        

        





