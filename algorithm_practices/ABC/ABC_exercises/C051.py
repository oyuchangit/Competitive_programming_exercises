# https://atcoder.jp/contests/abc051/tasks/abc051_c

sx, sy, tx, ty = map(int, input().split())

dx = tx - sx
dy = ty - sy

ans = ''

for a in range(dx):
    ans += 'R'

for b in range(dy + 1):
    ans += 'U'

for c in range(dx + 1):
    ans += 'L'

for d in range(dy + 1):
    ans += 'D'

ans += 'R'

ans += 'D'

for e in range(dx + 1):
    ans += 'R'

for f in range(dy + 1):
    ans += 'U'

for g in range(dx + 1):
    ans += 'L'

for h in range(dy):
    ans += 'D'

print(ans)