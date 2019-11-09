# https://atcoder.jp/contests/abc051/tasks/abc051_b

K_S = input().split()
K = int(K_S[0])
S = int(K_S[1])

total_xy = -1
expected_z = -1
range_xy = range(0, K + 1)
count_pattern = 0
for x in range_xy:
    for y in range_xy:
        expected_z = S - (x + y)
        if expected_z >=0 and expected_z <= K:
            count_pattern += 1

print(count_pattern)


# 以下もっとすっきり回答してた人のソース　ry1_1125
# zはfor文の中で宣言してる？pythonではそういうのもありなのか？
# そもそも宣言とかいう概念がないのか？
'''
k, s = map(int, input().split())
count = 0
for x in range(k + 1):
    for y in range(k + 1):
        z = s - x - y
        if 0 <= z <= k:
            count += 1
print(count)
'''