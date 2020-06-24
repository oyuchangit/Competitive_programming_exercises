# https://atcoder.jp/contests/abc134/tasks/abc134_b

N, D = map(int, input().split())

count = 0
ans = 1
for i in range(N):
    count += 1

    if count == D*2 + 2:
        ans += 1
        count = 1

print(ans)


#  123 4 567 890 1 234 5
#  ### # ### ### # ### #