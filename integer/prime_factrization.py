def factrize(x):
    factor = {}
    tmp = x
    i = 2
    while i ** 2 <= tmp:
        cnt = 0
        while tmp % i == 0:
            cnt += 1
            tmp //= i
        if cnt > 0:
            factor[i] = cnt
        i += 1
    if tmp != 1 or factor == {}:
        factor[tmp] = 1
    return factor
