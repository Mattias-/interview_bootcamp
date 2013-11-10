import sys

BANK_FEE = 0.5
(w, b) = sys.stdin.readline().split()
withdraw = int(w)
if withdraw % 5 == 0:
    balance = float(b)
    diff = balance - withdraw - BANK_FEE
    if diff >= 0:
        print "%0.2f" % diff
        sys.exit(0)
print b
