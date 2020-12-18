import bisect


def longest_increasing_subsequence(a):
    n = len(a)
    b = []
    for i in range(n):
        j = bisect.bisect_left(b, a[i])
        if j == n:
            b.append(a[i])
        else:
            b[j] = a[i]
    return b
