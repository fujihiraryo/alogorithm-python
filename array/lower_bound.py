def lower_bound(a, x, key=lambda i: i):
    n = len(a)
    i, j = -1, n
    while j - i > 1:
        k = (i + j) // 2
        if x <= key(a[k]):
            j = k
        else:
            i = k
    return j


def upper_bound(a, x, key=lambda i: i):
    n = len(a)
    i, j = -1, n
    while j - i > 1:
        k = (i + j) // 2
        if x < key(a[k]):
            j = k
        else:
            i = k
    return j
