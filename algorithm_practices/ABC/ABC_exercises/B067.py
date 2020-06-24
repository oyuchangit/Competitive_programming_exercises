# https://atcoder.jp/contests/abc067/tasks/abc067_b

N, K = map(int, input().split())
l_list = list(map(int, input().split()))

l_list.sort(reverse=True)

total_length = 0
i = 0
while i < K:
    total_length += l_list[i]
    i += 1

print(total_length)