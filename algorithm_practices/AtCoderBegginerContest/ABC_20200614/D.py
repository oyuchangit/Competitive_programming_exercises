N = int(input())
A_list = map(int, input().split())

A_list = sorted(A_list)
count = 0

soinsu_set = set()


def simple_factrization(n):
    table = []  # 素因数を格納する
    temp = n    # nを素因数で割っていった値を一時的に格納する

    for i in range(2, int(n**0.5//1) + 1):
        if temp % i == 0:
            cnt = 0

            while temp % i == 0:
                cnt += 1
                temp //= i

            table.append([i, cnt])

    if temp != 1:
        table.append([temp, 1])

    if temp == []:
        table.append([n, 1])

    return table


for i, A in enumerate(A_list):

    A_soinsu_list =simple_factrization(A)

    is_di = False

    for i in range(len(A_soinsu_list)):
        if A_soinsu_list[i][0] in soinsu_set:
            is_di = True

        soinsu_set.add(A_soinsu_list[i][0])

    if is_di:
        count += 1

ans = N - count
print(ans)

# 未完
