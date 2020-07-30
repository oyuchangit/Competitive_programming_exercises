# https://atcoder.jp/contests/abc171/tasks/abc171_c

import string

def getOrdOfAlphabet(s):
    return ord(s) - 64


def getAlphabetByNum(n):
    alphabets = string.ascii_lowercase
    return alphabets[n - 1]



N = int(input())

dog_name = ''

while N > 0:
    
    N -= 1
    mod = N % 26
    dog_name += getAlphabetByNum(mod + 1)
    N //= 26



print(dog_name[::-1])

