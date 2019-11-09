# https://atcoder.jp/contests/agc012/tasks/agc012_a

N = int(input())
a_list = list(map(int, input().split()))

a_list.sort()

target_total = 0
for j in range(N, 3 * N, 2):
    target_total += a_list[j]

print(target_total)

'''
n=int(input())
a=list(map(int,input().split()))
a=sorted(a,reverse=True)
print(sum(a[1:2*n:2]))
'''