n, W = map(int, input().split())
w_list = []
v_list = []

for i in range(n):
    w, v = map(int, input().split())
    w_list.append(w)
    v_list.append(v)

dp = [[-1 for i in range(W + 1)] for j in range(n + 1)]


def rec(i, max_w):

    if (dp[i][max_w] >= 0):
        return dp[i][max_w]

    result = 0

    if (i == n):
        result = 0

    elif (max_w < w_list[i]):
        result = rec(i + 1, max_w)

    else:
        result = max(rec(i + 1, max_w), rec(i + 1, max_w - w_list[i]) + v_list[i])

    dp[i][max_w] = result
    return result

print(rec(0, w))

    


# 未完