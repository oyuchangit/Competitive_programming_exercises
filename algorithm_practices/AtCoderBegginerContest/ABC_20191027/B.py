N = int(input())
able = False

for a in range(1, 10):
    for b in range(1, 10):
        if a * b == N:
            able = True
            break

if able:
    print('Yes')
else:
    print('No')
