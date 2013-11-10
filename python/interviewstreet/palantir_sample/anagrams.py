
import sys

def main():
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    if anagrams(s1, s2):
        print 'Anagrams!'
    else:
        print 'Not anagrams!'

def anagrams(s1, s2):
    li = list(s1)
    for c in s2:
        if c in li:
            li.remove(c)
        else:
            return False
    return len(li) == 0

if __name__ == '__main__':
    main()
