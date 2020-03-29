class Comb():
    # 同じnに対して何回もnCrをmod素数で計算するときに便利
    def __init__(self, n, p):
        # O(n)
        fct, inv = [1, 1], [1, 1]
        a, b = 1, 1
        for i in range(2, n + 1):
            a = (a * i) % p
            b = (b * pow(i, p - 2, p)) % p
            fct.append(a)
            inv.append(b)
        self.fct = fct
        self.inv = inv
        self.n = n
        self.p = p

    def calc(self, r):
        fct, inv = self.fct, self.inv
        if (r < 0 or n < r):
            return 0
        else:
            return fct[n] * inv[r] * inv[n - r] % p


def comb(n, r, p):
    # O(r)で計算したい場合はこっち
    x = 1
    for i in range(1, r + 1):
        x *= (n - i + 1) * pow(i, p - 2, p) % p
    return x % p


# テスト
n = 10**6
p = 10**9 + 7
cmb = Comb(n, p)
r = 10**5
print(cmb.calc(r))
print(comb(n, r, p))
