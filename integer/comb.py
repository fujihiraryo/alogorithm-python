class Comb0():
    # あらかじめO(k)の前計算をしておいてr<=kに対してnCrを高速に計算する
    def __init__(self, n, k=10**6, p=10**9 + 7):
        # num[i]=nPi
        # den[i]=(i!)^(-1)
        num, den = [1], [1]
        a, b = 1, 1
        for i in range(1, k + 1):
            a = (a * (n - i + 1)) % p
            b = (b * pow(i, p - 2, p)) % p
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
    def __init__(self, m=10**6, p=10**9 + 7):
        # fct[i]=i!
        # inv[i]=(i!)^(-1)
        fct, inv = [1], [1]
        a, b = 1, 1
        for i in range(1, m + 1):
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


def cmb(x, y, mod=10**9 + 7):
    if x <= y:
        return 0
    tmp = 1
    for i in range(y):
        tmp *= x - i
        tmp *= pow(y - i, mod - 2, mod)
        tmp %= mod
    return tmp


# パスカルの三角形(O(n))
n = 101
C = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    C[i][0] = 1
for i in range(1, n):
    for j in range(1, n):
        C[i][j] = C[i - 1][j - 1] + C[i - 1][j]


comb0 = Comb0(6)
print(comb0.calc(3))

comb1 = Comb1()
print(comb1.calc(6, 3))

print(cmb(6, 3))

print(C[6][3])
