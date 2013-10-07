
def main():
    a = list('abc')
    print a
    print all_subsets(a)


def all_subsets(li):
    if len(li) <= 0:
        return []
    elif len(li) == 1:
        return [li]
    mid = len(li)/2
    left = li[:mid]
    right = li[mid:]
    ls = all_subsets(left)
    rs = all_subsets(right)
    res = ls + rs
    print 'ls', ls
    print 'rs', rs
    for sub_left in ls:
        for sub_right in rs:
            res.append(sub_left + sub_right)
    return res




if __name__ == '__main__':
    main()
