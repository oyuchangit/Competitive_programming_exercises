from sys import stdin

S = input()
Q = int(input())

is_reversed = False

former_list = []
latter_list = []

for q in range(Q):
    T = stdin.readline()[:-1]

    if T == '1':
        if is_reversed:
            is_reversed = False
        else:
            is_reversed = True
    
    else:
        t, f, c = T.split()
        if (f == '1' and is_reversed == False) or (f == '2' and is_reversed == True):
            former_list.append(c)
        else:
            latter_list.append(c)

if is_reversed:
    latter_list = ''.join(reversed(latter_list))
    former_list = ''.join(former_list)
    S = ''.join(list(reversed(S)))
    S = ''.join([latter_list, S, former_list])

else:
    former_list = ''.join(reversed(former_list))
    latter_list = ''.join(latter_list)
    S = ''.join([former_list, S, latter_list])

print(S) 
