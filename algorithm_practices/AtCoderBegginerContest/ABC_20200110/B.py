N = int(input())
S = input()

count = 0

while True:
    index_ABC = S.find('ABC')
    if index_ABC != -1:
        S = S[:index_ABC] + S[index_ABC + 3:]
        count += 1
    else:
        break

print(count)