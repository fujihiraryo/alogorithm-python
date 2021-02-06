from collections import defaultdict


class Sieve:
    def __init__(self, n):
        table = [i for i in range(n)]
        for i in range(2, n):
            if table[i] != i:
                continue
            for j in range(2 * i, n, i):
                table[j] = i
        self.table = table

    def factorize(self, x):
        y = x
        factor = defaultdict(int)
        while y > 1:
            factor[self.table[y]] += 1
            y //= self.table[y]
        return factor


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
        if not is_prime[i]:
            continue
        for j in range(2 * i, n, i):
            is_prime[j] = 0
    return is_prime
