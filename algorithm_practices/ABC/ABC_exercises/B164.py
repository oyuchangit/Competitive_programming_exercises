# https://atcoder.jp/contests/abc164/tasks/abc164_b

# 高橋君のモンスターは体力が A で攻撃力が B
# 青木君のモンスターは体力が C で攻撃力が D

A, B, C, D = map(int, input().split())

while (A >= 0 or C >= 0):
    
    C -= B

    if C <= 0:
        print('Yes')
        exit()

    A -= D

    if A <= 0:
        print('No')
        exit()

