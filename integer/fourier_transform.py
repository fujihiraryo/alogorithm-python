class FFT:
    def __init__(self, n=262144, p=347078657, w=13):
        self.n = n
        self.p = p
        self.w = w
        self.rn = pow(n, p - 2, p)
        self.rw = pow(w, p - 2, p)

    def base(self, a, n, w):
        if n == 1:
            return a
        p = self.p
        for i in range(n - len(a)):
            a.append(0)
        f0 = self.base(a[0::2], n // 2, pow(w, 2, p))
        f1 = self.base(a[1::2], n // 2, pow(w, 2, p))
        x = 1
        f = []
        for i in range(n):
            f.append((f0[i % (n // 2)] + x * f1[i % (n // 2)]) % p)
            x = (x * w) % p
        return f

    def fft(self, a):
        return self.base(a, self.n, self.w)

    def ift(self, a):
        f = self.base(a, self.n, self.rw)
        return list(map(lambda x: (x * self.rn) % self.p, f))

    def conv(self, a, b):
        fa = self.fft(a)
        fb = self.fft(b)
        fc = [fa[i] * fb[i] for i in range(self.n)]
        return self.ift(fc)
