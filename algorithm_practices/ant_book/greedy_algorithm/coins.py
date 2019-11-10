'''     p. 42
貪欲法 (Greedy algorithm) 

-硬貨の問題-
1円玉、5円玉、10円玉、50円玉、100円玉、500円玉が、
それぞれC1, C5, C10, C50, C100, C500枚ずつあります。
できるだけ少ない枚数の硬貨でA円を支払いたいと考えています。
何枚の硬貨を出す必要があるでしょうか？
なお、そのような支払い方は少なくとも1つは存在するとします。

-制約-
・0 <= C1, C5, C10, C50, C100, C500 <= 10^9

-例-
入力
C1 = 3, C5 = 2, C10 = 1, C50 = 3, C100 = 0, C500 = 2
A = 620

出力
6
'''


# コインの金額
value_of_coins = [1, 5, 10, 50, 100, 500]

# 入力
C = list(map(int, input().split()))
A = int(input())

coins = 0

for i in reversed(range(6)):
    # コインiを使う枚数
    coins_i = min(A // value_of_coins[i], C[i])
    A -= coins_i * value_of_coins[i]
    coins += coins_i

print(coins)