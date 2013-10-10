
def reverse_recursive(a):
    if len(a)>1:
       return reverse_recursive(a[1:]) + a[0]
    else:
       return a

def reverse_inplace(s):
    a = list(s)
    l = len(a) - 1
    for i in xrange(l/2):
        tmp = a[i]
        a[i] = a[l-i]
        a[l-i] = tmp
    return "".join(a)
