class FFT():
    def __init__(self, n, p, w):
        # pは素数で, wは1のn乗根(mod p)
        # 例:(n,p,w)=(4,5,2),(8,17,2),(262144,347078657,13)
        self.n = n
        self.p = p
        self.w = w
        self.rn = pow(n, p-2, p)
        self.rw = pow(w, p-2, p)

    def base(self, A, n, w):
        p = self.p
        for i in range(n-len(A)):
            A.append(0)
        if n == 1:
            return A
        F0 = self.base(A[0::2], n//2, pow(w, 2, p))
        F1 = self.base(A[1::2], n//2, pow(w, 2, p))
        x = 1
        F = []
        for i in range(n):
            f = (F0[i % (n//2)] + x * F1[i % (n//2)]) % p
            x = (x * w) % p
            F.append(f)
        return F

    def fft(self, A):
        return self.base(A, self.n, self.w)

    def ift(self, A):
        F = self.base(A, self.n, self.rw)
        return [(f * self.rn) % self.p for f in F]
