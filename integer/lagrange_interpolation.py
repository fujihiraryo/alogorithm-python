MOD = 10 ** 9 + 7


class Lagrange:
    def __init__(self, lst):
        self.lst = lst

    def _f(self, j, x):
        prd = 1
        for i, (xi, yi) in enumerate(self.lst):
            if j != i:
                prd *= x - xi
                prd %= MOD
        return prd

    def p(self, x):
        tmp = 0
        for i, (xi, yi) in enumerate(self.lst):
            tmp += yi * (self._f(i, x) * pow(self._f(i, xi), MOD - 2, MOD))
            tmp %= MOD
        return tmp


if __name__ == "__main__":
    n = 5

    def p(x):
        tmp = 0
        for i in range(n):
            tmp += (i + 1) * x ** (n - i)
            tmp %= MOD
        return tmp

    lst = [(x, p(x)) for x in range(n + 1)]
    lag = Lagrange(lst)
    for x in range(n, 3 * n):
        print(lag.p(x), p(x))
