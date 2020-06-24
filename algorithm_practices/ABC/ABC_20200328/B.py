X = int(input())

count_500 = X // 500
count_5 = (X-count_500*500) // 5

u = count_500 * 1000 + count_5 * 5
print(u)