class SegmentTree:
    def __init__(self, a, ide, idf, fold, compose, apply):
        self.size = len(a)
        self.ide = ide
        self.fold = fold
        self.apply = apply
        self.data = [self.ide] * (self.size << 1)
        self.memo = [self.idf] * (self.size << 1)
        self.data[self.size :] = a
        for k in range(1, self.size)[::-1]:
            self.data[k] = self.fold(self.data[k << 1], self.data[k << 1 | 1])

    def __covered_index(self, i, j):
        i0 = i + self.size
        j0 = j + self.size
        while i0 < j0:
            if i0 & 1:
                yield i0
                i0 += 1
            if j0 & 1:
                yield j0 - 1
            i0 >>= 1
            j0 >>= 1

    def point_apply(self, i, f):
        i0 = i + self.size
        self.data[i0] = self.apply(f, self.data[i0])
        while i0:
            i0 >>= 1
            self.data[i0] = self.fold(self.data[i0 << 1], self.data[i0 << 1 | 1])

    def range_fold(self, i, j):
        x = self.ide
        for k in self.__covered_index(i, j):
            x = self.fold(x, self.data[k])
        return x


MOD = 998244353
BIT = 30
MASK = (1 << BIT) - 1


def encode(x0, x1):
    return (x0 << BIT) + x1


def decode(x):
    return x >> BIT, x & MASK


def fold(x, y):
    x0, x1 = decode(x)
    y0, y1 = decode(y)
    z0 = (x0 + y0) % MOD
    z1 = x1 + y1
    return encode(z0, z1)


def apply(f, x):
    f0, f1 = decode(f)
    x0, x1 = decode(x)
    y0 = (f0 * x0 + f1 * x1) % MOD
    y1 = x1
    return encode(y0, y1)
