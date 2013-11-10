import sys

(n, k) = [int(x) for x in sys.stdin.readline().split()]
i = 0
lines = sys.stdin.readlines()
#for line in lines:
#    if int(line) % k == 0:
#        i += 1
for _ in xrange(n):
    v = int(sys.stdin.readline())
    if v % k == 0:
        i += 1
print i
