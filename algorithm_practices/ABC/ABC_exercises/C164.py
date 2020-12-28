# https://atcoder.jp/contests/abc164/tasks/abc164_c


N = int(input())

S_set = set()

for i in range(N):
    S = input()
    S_set.add(S)

ans = len(S_set)

print(ans)


