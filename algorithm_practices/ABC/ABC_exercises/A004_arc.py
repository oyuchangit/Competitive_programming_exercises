# https://atcoder.jp/contests/arc004/tasks/arc004_1
import math

N = int(input())

x_y = []
x_y_list = []
for i in range(N):
    x_y = list(map(int, input().split()))
    x_y_list.append([x_y[0], x_y[1]])

diff = 0
max_diff = 0
range_for = range(N)
for n in range_for:
    for m in range_for:
        diff = math.sqrt(((x_y_list[n][0] - x_y_list[m][0])**2 + (x_y_list[n][1] - x_y_list[m][1])**2))
        
        if max_diff < diff:
            max_diff = diff

print(max_diff)