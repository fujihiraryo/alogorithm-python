def product(a, b, p=10 ** 9 + 7):
    n = len(a)
    c = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = sum([a[i][k] * b[k][j] for k in range(n)]) % p
    return c


def matpow(a, k, p=10 ** 9 + 7):
    if k == 1:
        return a
    if k % 2 == 0:
        b = matpow(a, k // 2)
        return product(b, b, p=p)
    return product(a, matpow(a, k - 1), p=p)
