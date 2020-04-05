# https://atcoder.jp/contests/abc066/tasks/abc066_b

S = input()
S_len = len(S)

while True:
    S = S[:S_len - 2]
    S_len = len(S)

    middle = S_len // 2

    if S[:middle] == S[middle:]:
        print(S_len)
        exit()