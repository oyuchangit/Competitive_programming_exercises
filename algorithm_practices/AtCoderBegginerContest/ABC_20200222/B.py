import math

N, K = map(int, input().split())

log = math.log(N, K)
print(int(log) + 1)