# https://atcoder.jp/contests/abc057/tasks/abc057_b

N, M = map(int, input().split())

stu_list = []
for i in range(N):
    stu = list(map(int, input().split()))
    stu_list.append(stu)

chkpoint_list = []
for i in range(M):
    chkpoint = list(map(int, input().split()))
    chkpoint_list.append(chkpoint)

INF = 1000000000
for stu in stu_list:
    min_distance = INF
    for m in range(M):
        distance = abs(chkpoint_list[m][0] - stu[0]) + abs(chkpoint_list[m][1] - stu[1])

        if distance < min_distance:
            min_distance = distance
            ans = m + 1

    print(ans)
