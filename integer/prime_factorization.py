def factorize(x):
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


def prime_sieve(n):
    is_prime = [1] * n
    is_prime[0], is_prime[1] = 0, 0
    for i in range(2, n):
        if is_prime[i]:
            for j in range(2 * i, n, i):
                is_prime[j] = 0
    for p in range(n):
        if is_prime[p]:
            yield p
