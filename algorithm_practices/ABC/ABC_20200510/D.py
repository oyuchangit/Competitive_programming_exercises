N, K = map(int, input().split())
A_list = list(map(int, input().split()))

l_set = set()
l_set.add(0)
tele_list = [0]
current_city = 0


for i in range(N):
    current_city = A_list[current_city] - 1

    if current_city in l_set:
        break

    else:

        tele_list.append(current_city)
        l_set.add(current_city)

len_tele_list = len(tele_list)
index_last = len_tele_list % K - 1

print(tele_list[index_last] + 1)

# 未完