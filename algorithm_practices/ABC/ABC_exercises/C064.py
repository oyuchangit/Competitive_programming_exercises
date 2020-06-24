# https://atcoder.jp/contests/abc064/tasks/abc064_c

N = int(input())
a_list = list(map(int, input().split()))

rate_count_list = [0] * 8   # 各色の人数
count_over_red = 0          # 赤色以上の人数

for a in a_list:

    # aの色を判定
    # 赤色以上の場合
    if a >= 3200:
        count_over_red += 1

    # 灰色から順に見ていく
    else:
        for i in range(8):
            if i == 0:
                min_in_rate = 1
            else:
                min_in_rate = 400 * i

            max_in_rate = 400 * (i + 1)

            if min_in_rate <= a < max_in_rate:
                rate_count_list[i] = 1
                break

ans_min = sum(rate_count_list)

ans_max = ans_min + count_over_red

print(str(max(ans_min, 1)) + ' ' + str(ans_max))

