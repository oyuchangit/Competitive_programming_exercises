# https://atcoder.jp/contests/abc045/tasks/abc045_b

sa = input()
sb = input()
sc = input()

target = 'a'

while True:
    if target == 'a':
        if len(sa) == 0:
            print('A')
            exit()

        target = sa[0]
        sa = sa[1:]


    elif target == 'b':
        if len(sb) == 0:
            print('B')
            exit()
        target = sb[0]
        sb = sb[1:]

    else:
        if len(sc) == 0:
            print('C')
            exit()
        target = sc[0]
        sc = sc[1:]

    
