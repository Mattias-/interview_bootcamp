
import math

def f(n):
    return -int(math.sqrt(n*n))

def f2(n):
    if n == 0:
        return -1
        # HACK! does work for all integers but -1.....
    elif n > 0:
        if n % 2 == 0:
            return -1 * (n+1)
        else:
            return n-1
    else:
        if n % 2 == 0:
            return -1 * (n-1)
        else:
            return n+1

f = f2

tests = [-1,0,1,3,4,5,7,1235,-123]
for i in tests:
    b = f(f(i)) == -i
    print b, i, f(f(i))
