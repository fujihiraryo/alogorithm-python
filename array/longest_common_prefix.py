def lcp(s):
    n = len(s)
    a = [0] * n
    j = 0
    for i in range(1, n):
        if i + a[i - j] < j + a[j]:
            a[i] = a[i - j]
        else:
            k = max(0, a[j] - i + j)
            while i + k < n and s[k] == s[i + k]:
                k += 1
            a[i] = k
            j = i
    a[0] = n
    return a
