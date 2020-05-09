X = int(input())

for i in range(-200, 400):
    for j in range(-200, 400):
        if i ** 5 - j ** 5 == X:
            print(i, j)
            exit()

        elif j ** 5 - i ** 5 == X:
            print(j, i)
            exit()