import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


N = int(input())
S, T = input().split()
ans_str = ''

for i in range(N):
    ans_str += S[i] + T[i]

print(ans_str)