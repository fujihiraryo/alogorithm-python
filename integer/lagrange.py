mod = 10**9 + 7


class Lagrange:
    def __init__(self, lst):
        self.lst = lst
        self.mod = mod

    def f(self, j, x):
        prd = 1
        for i, (xi, yi) in enumerate(self.lst):
            if j != i:
                prd *= (x - xi)
                prd %= self.mod
        return prd

    def P(self, x):
        tmp = 0
        for i, (xi, yi) in enumerate(self.lst):
            tmp += yi * (self.f(i, x) *
                         pow(self.f(i, xi), self.mod - 2, self.mod))
            tmp %= self.mod
        return tmp


if __name__ == "__main__":
    n = 5

    def P(x):
        tmp = 0
        for i in range(n):
            tmp += (i + 1) * x**(n - i)
            tmp %= mod
        return tmp

    lst = [(x, P(x)) for x in range(n + 1)]
    lag = Lagrange(lst)
    for x in range(n, 3 * n):
        print(lag.P(x), P(x))
