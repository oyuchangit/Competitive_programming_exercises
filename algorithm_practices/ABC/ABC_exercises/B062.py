# https://atcoder.jp/contests/abc062/tasks/abc062_b

H, W = map(int, input().split())

ans = []

for i in range(H):
    ans_ = input()
    ans.append(ans_)

ans_t_ = '#' * (W + 2)
print(ans_t_)

for t in ans:
    ans_t = '#' + t + '#'
    print(ans_t)

print(ans_t_)