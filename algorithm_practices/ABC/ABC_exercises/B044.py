# https://atcoder.jp/contests/abc044/tasks/abc044_b

w = input()

w_dic = {}

for i in w:
    if i in w_dic:
        w_dic[i] += 1
    else:        
        w_dic[i] = 1

ans = [k for k, v in w_dic.items() if v % 2 != 0]

if len(ans) == 0:
    print('Yes')
else:
    print('No')