N, K = map(int, input().split())

sunuke_list = [0] * (N + 1)
d_list = []
A_list = []

for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))

    for a in A:
        sunuke_list[a] += 1

print(sunuke_list.count(0) - 1)

    


