class Comb0():
    # あらかじめO(k)の前計算をしておいてr<=kに対してnCrを高速に計算する
    def __init__(self, n, k=10**6, p=10**9+7):
        # num[i]=nPi
        # den[i]=(i!)^(-1)
        num, den = [1], [1]
        a, b = 1, 1
        for i in range(1, k+1):
            a = (a*(n-i+1)) % p
            b = (b*pow(i, p-2, p)) % p
            num.append(a)
            den.append(b)
        self.num = num
        self.den = den
        self.n = n
        self.p = p

    def calc(self, r):
        num, den = self.num, self.den
        if r < 0 or self.n < r:
            return 0
        return (num[r] * den[r]) % self.p


class Comb1():
    # あらかじめO(m)の前計算をしておいてn<=mに対してnCrを高速に計算する
    def __init__(self, m=10**6, p=10**9+7):
        # fct[i]=i!
        # inv[i]=(i!)^(-1)
        fct, inv = [1], [1]
        a, b = 1, 1
        for i in range(1, m+1):
            a = (a * i) % p
            b = (b * pow(i, p - 2, p)) % p
            fct.append(a)
            inv.append(b)
        self.fct = fct
        self.inv = inv
        self.p = p

    def calc(self, n, r):
        fct, inv = self.fct, self.inv
        if r < 0 or n < r:
            return 0
        return (fct[n] * inv[r] * inv[n - r]) % self.p


cmb = Comb0(10**9)
print(cmb.calc(10**5))

cmb = Comb0(6)
print(cmb.calc(3))

cmb = Comb1()
print(cmb.calc(6, 3))
