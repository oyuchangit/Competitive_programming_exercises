N = int(input())
X_list = list(map(int, input().split()))

min_X = min(X_list)
max_X = max(X_list)

min_cost = 0
for p in range(min_X, max_X + 1):

    cost = 0
    for i in range(N):
        cost += (X_list[i] - p) ** 2
    
    if cost < min_cost or min_cost == 0:
        min_cost = cost

print(min_cost)