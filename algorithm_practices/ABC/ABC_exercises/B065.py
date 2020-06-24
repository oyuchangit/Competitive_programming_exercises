# https://atcoder.jp/contests/abc065/tasks/abc065_b

N = int(input())
a_list = []

for i in range(N):
    a = int(input())
    a_list.append(a)


current = 0
count = 0
for _ in range(N):
    current = a_list[current] - 1
    count += 1

    if current == 1:
        print(count)
        exit()

print(-1)