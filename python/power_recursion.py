

# write a recursive function that calculates x to the power of y


def pow1(x, y):
    if y > 1:
        return x * pow(x, y-1)
    else:
        return 1


def pow2(x, y):
    if y == 2:
        return x*x
    else:
        rt = pow2(x, y/2)
        if y % 2 == 0:
            return rt * rt
        else:
            return x * rt * rt

print pow(2,8)
print pow(10, 5)

print pow1(2,8)
print pow1(10, 5)

print pow2(2,8)
print pow2(10, 5)

