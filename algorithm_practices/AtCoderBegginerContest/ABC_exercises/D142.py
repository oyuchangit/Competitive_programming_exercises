# https://atcoder.jp/contests/abc142/tasks/abc142_d

A, B = map(int, input().split())

# 素因数分解　何個あるかどうかを返却
def factrization(n, B):
    table = []  # 素因数を格納する
    temp = n    # nを素因数で割っていった値を一時的に格納する
    value = 0

    for i in range(2, int(n**0.5//1) + 1):
        if temp % i == 0:
            cnt = 0

            while temp % i == 0:
                cnt += 1
                temp //= i

            table.append([i, cnt])

            if B % i == 0:
                value += 1


    if temp != 1:
        table.append([temp, 1])

        if B % temp == 0:
            value += 1

    if temp == []:
        table.append([n, 1])

        if B % n == 0:
            value += 1

    return value


value = factrization(A, B)

print(value + 1)


# おまけ
# 純粋な素因数分解（↑のは、この問題用の素因数分解）

# 素因数分解

# def simple_factrization(n):
#     table = []  # 素因数を格納する
#     temp = n    # nを素因数で割っていった値を一時的に格納する

#     for i in range(2, int(n**0.5//1) + 1):
#         if temp % i == 0:
#             cnt = 0

#             while temp % i == 0:
#                 cnt += 1
#                 temp //= i

#             table.append([i, cnt])

#     if temp != 1:
#         table.append([temp, 1])

#     if temp == []:
#         table.append([n, 1])

#     return table


# f = simple_factrization(n)

