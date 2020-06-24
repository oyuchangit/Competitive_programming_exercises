from decimal import *

A, B = map(float, input().split())

ans = Decimal(str(A)) * Decimal(str(B))
ans = str(ans)
i = ans.find('.')
ans = ans[:i]


print(ans)