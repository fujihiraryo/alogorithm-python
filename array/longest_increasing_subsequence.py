import bisect


def lis(a):
    b = []
    for x in a:
        i = bisect.bisect_left(b, x)
        if i == len(b):
            b.append(x)
        else:
            b[i] = x
    return len(b)
