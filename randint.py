from random import *

def randint(n, m):
    if m < n:
        raise Error
    else:
        b = getrandbits(10)
        while m < b < n:
            b = getrandbits(10)
        return b

