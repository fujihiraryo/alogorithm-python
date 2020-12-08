MOD = 10 ** 9 + 7


def inverse(x):
    return pow(x, MOD - 2, MOD)


class Lagrange:
    def __init__(self, arr):
        self.arr = arr

    def __call__(self, x):
        res = 0
        for i, (xi, yi) in enumerate(self.arr):
            a, b = 1, 1
            for j, (xj, yj) in enumerate(self.arr):
                if i == j:
                    continue
                a = a * (x - xj) % MOD
                b = b * (xi - xj) % MOD
            res = (res + yi * a * inverse(b)) % MOD
        return res
