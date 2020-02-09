a, b = input().split()

a_ = ''
b_ = ''

for i in range(int(b)):
    a_ = a_ + a

for j in range(int(a)):
    b_ = b_ + b

if a_ < b_:
    print(a_)
else:
    print(b_)
