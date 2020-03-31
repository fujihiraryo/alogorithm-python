class Sieve():
    # 最初にn以下の素数を列挙する
    # n=10^5くらいまでなら余裕
    def __init__(self, n):
        X = list(range(2, n + 1))
        f = {}
        while X[0] <= n**0.5:
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

    def factrize(self, n):
        f = self.primes
        tmp = n
        g = {}
        while f[tmp]:
            try:
                g[f[tmp]] += 1
            except:
                g[f[tmp]] = 1
            tmp = tmp // f[tmp]
        try:
            g[tmp] += 1
        except:
            g[tmp] = 1
        return g


# テスト
n = 10**5
sieve = Sieve(n)
print(sieve.factrize(3664))
print(sieve.factrize(28781))
print(sieve.factrize(10001))