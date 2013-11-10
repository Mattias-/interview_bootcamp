
import sys


def f(i, n, k):
    return n - ((i%k) + 1) * n/k + i/k

def min_shuffles(n, k):
    counter = 0
    i = 0
    prev = {}
    while True:
        r = f(i, n, k)
        counter += 1
        if r == 0:
            return counter
        else:
            if prev.get(r, False):
                return -1
            else:
                prev[r] = True
                if counter > n:
                    return -1
        i = r



test_cases = int(sys.stdin.readline().rstrip())
for i in xrange(test_cases):
    (n, k) = [int(x) for x in sys.stdin.readline().split()]
    print min_shuffles(n, k)

