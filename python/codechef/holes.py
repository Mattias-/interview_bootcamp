import sys


hole_map = {
    'A': 1,
    'B': 2,
    'D': 1,
    'O': 1,
    'P': 1,
    'Q': 1,
    'R':1
}
words = int(sys.stdin.readline())
for _ in xrange(words):
    res = 0
    word = sys.stdin.readline()
    for letter in word:
        res += hole_map.get(letter, 0)
    print res
