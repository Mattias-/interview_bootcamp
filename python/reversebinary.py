
import sys
import math

def main():
    i = int(sys.stdin.readline().strip())
    print to_dec(to_bin2(i)[::-1])


def to_bin(dec):
    i = 1
    while dec >= 2**i:
        i += 1
    i -= 1
    s = ""
    while i >= 0:
        if dec >= 2**i:
            dec -= 2**i
            s += "1"
        else:
            s += "0"
        i -= 1
    return s


def to_bin2(dec):
    exp = int(math.floor(math.log(dec, 2)))
    s = ''
    while exp >= 0:
        if dec >= 2**exp:
            dec -= 2**exp
            s += "1"
        else:
            s += "0"
        exp -= 1
    #for i in range(exp, 0):
    #    print i
    return s


def to_dec(b):
    s = str(b)[::-1]
    ss = 0
    for i, x in enumerate(s):
        ss += int(x) * 2**i
    return ss


def to_dec2(b):
    f1 = lambda (x, y): y * 2**x
    m = map(f1, reversed(enumerate(list(b))))
    r = sum(m)
    return r



if __name__ == '__main__':
    main()
