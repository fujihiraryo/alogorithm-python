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

[
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    53,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    103,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
    211,
    223,
    227,
    229,
    233,
    239,
    241,
    251,
    257,
    263,
    269,
    271,
    277,
    281,
    283,
    293,
    307,
    311,
    313,
    317,
    331,
    337,
    347,
    349,
    353,
    359,
    367,
    373,
    379,
    383,
    389,
    397,
    401,
    409,
    419,
    421,
    431,
    433,
    439,
    443,
    449,
    457,
    461,
    463,
    467,
    479,
    487,
    491,
    499,
    503,
    509,
    521,
    523,
    541,
    547,
    557,
    563,
    569,
    571,
    577,
    587,
    593,
    599,
    601,
    607,
    613,
    617,
    619,
    631,
    641,
    643,
    647,
    653,
    659,
    661,
    673,
    677,
    683,
    691,
    701,
    709,
    719,
    727,
    733,
    739,
    743,
    751,
    757,
    761,
    769,
    773,
    787,
    797,
    809,
    811,
    821,
    823,
    827,
    829,
    839,
    853,
    857,
    859,
    863,
    877,
    881,
    883,
    887,
    907,
    911,
    919,
    929,
    937,
    941,
    947,
    953,
    967,
    971,
    977,
    983,
    991,
    997,
]
