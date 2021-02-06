def divisor(n):
    res = set()
    i = 1
    while i ** 2 <= n:
        if n % i == 0:
            res.add(i)
            res.add(n // i)
        i += 1
    return res
