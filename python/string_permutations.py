
def main():
    a = "abcde"
    p = permutations(a)
    print p


def permutations(s):
    if len(s) <= 1:
        return [s]
    char = s[0]
    perms = permutations(s[1:])
    result = []
    for perm in perms:
        for i in xrange(len(s)):
            r = perm[:i] + char + perm[i:]
            result.append(r)
    return result

if __name__ == '__main__':
    main()
