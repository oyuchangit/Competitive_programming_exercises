# https://atcoder.jp/contests/abc105/tasks/abc105_b

# total price
N = int(input())

cake_price = 4
donut_price = 7

max_cake = N // cake_price
max_donut = N // donut_price

isJustN = False
if max_cake * cake_price == N or max_donut * donut_price == N:
    isJustN = True
else:
    for c in range(1, max_cake + 1):
        for d in range(1, max_donut + 1):
            total_price = cake_price * c + donut_price * d
            if total_price == N:
                isJustN = True
                break

Result = ''
Result = 'Yes' if isJustN == True else 'No'
print(Result)
