S = input()

if len(S) % 2 != 0:
    middle = len(S) // 2
    S = S[:middle] + S[middle + 1:]

half_S = int(len(S)/2)

first_S = S[:half_S]
second_S = S[half_S:]
second_S = second_S[::-1]

count = 0
for i in range(len(first_S)):
    if first_S[i] != second_S[i]:
        count += 1

print(count)

