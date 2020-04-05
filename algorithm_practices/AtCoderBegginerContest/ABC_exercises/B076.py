# https://atcoder.jp/contests/abc076/tasks/abc076_b

N = int(input())
K = int(input())

min_ans = -1

def dfs(n, count):
    global min_ans

    if count == N:
        if n < min_ans or min_ans < 0:
            min_ans = n
        return

    dfs(n * 2, count + 1)
    dfs(n + K, count + 1)

dfs(1, 0)
print(min_ans)