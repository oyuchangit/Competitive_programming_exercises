# https://atcoder.jp/contests/abc054/tasks/abc054_a

A, B = map(int, input().split())
Alice = 'Alice'
Bob = 'Bob'
Draw = 'Draw'

if A == B:
    print(Draw)
elif A == 1 and B != 1:
    print(Alice)
elif A != 1 and B == 1:
    print(Bob)
elif A > B:
    print(Alice)
elif A < B:
    print(Bob)

