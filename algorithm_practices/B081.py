# https://atcoder.jp/contests/abc081/tasks/abc081_b

N = int(input())
A = list(map(int, input().split()))

# リスト内の要素に奇数が含まれているかどうかを判断する
# 戻り値：Boolean
def judge_hasOdd(A):
    hasOdd = False
    for a in A:
        if a % 2 == 0:
            continue
        else:
            hasOdd = True
            break
    return hasOdd


# リスト内の全要素を２で割る
# リスト内に奇数が現れるまで上記操作を繰り返す
count = 0
while True:
    if judge_hasOdd(A):
        break
    else:
        A = list(map(lambda x: x/2, A))
        count += 1
print(count)

