
def main():
    l1 = [34,56,7,5,3,6,78,9,43,23445689,34]
    l2 = [34,45,76,4,23,456,456,34,43234,3]
    print l1
    print l2
    print common_elements(l1, l2)


def common_elements(l1, l2):
    # Time complexity O(N + M)
    lookup = {}
    for e in l1:
        lookup[e] = True
    res = []
    for e in l2:
        if lookup.get(e, False):
            res.append(e)
            lookup[e] = False
    return res


if __name__ == '__main__':
    main()
