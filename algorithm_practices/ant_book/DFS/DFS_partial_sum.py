'''     p. 34
深さ優先探索 (DFS: Depth-First Search) 

-部分和問題-
整数a1, a2, ..., an が与えられます。
その中からいくつか選び、その和をちょうどkにすることができるかを判定しなさい。

-制約-
・1 <= n <= 20
・-10^8 <= ai <= 10^8
・-10^8 <= k <= 10^8

-例-
入力
n = 4
a = {1, 2, 4, 7}
k = 13

出力
Yes


入力
n = 4
a = {1, 2, 4, 7}
k = 15

出力
No
'''

import time

# 入力
n = int(input())
a = list(map(int, input().split()))
k = int(input())


# iまででsumを作って、残りi以降を調べる
def dfs(i, sum):
    # n個決め終わったら、今までの和sumがkと等しいかを返す
    if i == n:
        print (sum)
        return sum == k
    
    # a[i]を使わない場合
    if dfs(i + 1, sum):
        return True
    
    # a[i]を使う場合
    if dfs(i + 1, sum + a[i]):
        return True
    
    # a[i]を使う使わないにかかわらずkが作れないのでfalseを返す
    return False


# 時間計測用 開始時間
_start_time = time.time()


if dfs(0, 0):
    print('Yes')
else:
    print('No')


# 時間計測用 実行時間
_elapsed_time = time.time() - _start_time
print(_elapsed_time * 1000)

