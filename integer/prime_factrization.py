def factrize(x):
    # 試し割りによるxの素因数分解
    f = {}
    tmp = x
    i = 2
    while i ** 2 <= tmp:
        cnt = 0
        while tmp % i == 0:
            cnt += 1
            tmp = tmp // i
        if cnt > 0:
            f[i] = cnt
        i += 1
    if tmp != 1 or f == {}:
        f[tmp] = 1
    return f


class Sieve:
    # エラトステネスの篩
    def __init__(self, n):
        # f[x]=0ならxは素数
        # f[x]はxの最小の素因数
        X = list(range(2, n + 1))
        f = {}
        while X[0] ** 2 <= n:
            tmp = X[0]
            f[tmp] = 0
            X_new = []
            for x in X[1:]:
                if x % tmp == 0:
                    f[x] = tmp
                else:
                    X_new.append(x)
            X = X_new
        for x in X:
            f[x] = 0
        self.primes = f

    def factrize(self, x):
        # n未満のxを素因数分解
        f = self.primes
        tmp = x
        g = {}
        while f[tmp]:
            try:
                g[f[tmp]] += 1
            except BaseException:
                g[f[tmp]] = 1
            tmp = tmp // f[tmp]
        try:
            g[tmp] += 1
        except BaseException:
            g[tmp] = 1
        return g


# テスト
print(Sieve(100).primes)
n = 10 ** 5
sieve = Sieve(n)
print(sieve.factrize(3664))
print(factrize(3664))
print(sieve.factrize(28781))
print(factrize(28781))
print(sieve.factrize(10001))
print(factrize(11223344556677889900))
