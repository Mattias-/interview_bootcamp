
import pprint

a = [1,2,5,453,23,23,56,6,34,3,65,56,3,34,76,5,34,234,4,78,8,4,3,3,6,7]

def kth_largest(a, k):
# O(n log k)
    largest = k * [a[0]]
    for e in a[1:]:
        if e < largest[k-1]:
            continue
        elif e > largest[0]:
            largest.insert(0, e)
            largest.pop(k-1)
        else:
            low = 0
            high = k-1
            mid = (low + high)/2

            while high - low > 1:
                if e <= largest[mid]:
                    low = mid
                    mid = (low + high)/2
                elif e > largest[mid]:
                    high = mid
                    mid = (low + high)/2
            if e >= largest[mid]:
                largest.pop(k-1)
                largest.insert(mid, e)
            else:
                largest.pop(k-1)
                largest.insert(mid+1, e)
    print largest
    print sorted(a, reverse=True)
    return largest[-1]
kth_largest(a, 5)

def kth_largest_2(a, k):
    # int values between 0 and N
    # O(n) , cool! Much memory, ints, small range.
    N = 1000
    memo_array = N * [0]
    for n in a:
        memo_array[n] += 1
    kth = 0
    for i in xrange(1, N-1):
        kth += memo_array[N-i]
        if kth >= k:
            return N-i

print kth_largest_2(a, 5)
