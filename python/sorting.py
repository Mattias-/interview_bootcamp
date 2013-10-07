
def main():
    a = [5,3,3,6,7,5,3,3,5]
    b = [4,3,2,5]
    print merge_sort(a)
    print quick_sort(a)


def merge_sort(li):
    if len(li) <= 1:
        return li
    mid = len(li)/2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])
    i_r = i_l = 0
    res = []
    while i_r < len(right) and i_l < len(left):
        if left[i_l] < right[i_r]:
            res.append(left[i_l])
            i_l += 1
        else:
            res.append(right[i_r])
            i_r += 1
    res.extend(left[i_l:])
    res.extend(right[i_r:])
    return res


def quick_sort(li):
    if len(li) <= 1:
        return li
    pivot = li.pop(0)
    left = []
    right = []
    for e in li:
        if e < pivot:
            left.append(e)
        else:
            right.append(e)
    return quick_sort(left) + [pivot] + quick_sort(right)


# Bucket sort, many items might be the same, given range

# Merge sort, in place, iterative


if __name__ == '__main__':
    main()
