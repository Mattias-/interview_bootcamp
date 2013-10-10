

# Using any language you want (even pseudocode), write a program or subroutine
# that prints the numbers from 1 to 100, each number on a line, except for every
# third number write "fizz", for every fifth number write "buzz", and if a
# number is divisible by both 3 and 5 write "fizzbuzz".


def fb():
    for i in xrange(1, 100):
        s = ""
        if i % 3 == 0:
            s = "fizz"
        if i % 5 == 0:
            s += "buzz"
        if not s:
            print i
        else:
            print s

fb()
