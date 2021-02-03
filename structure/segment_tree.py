class SegmentTree:
    def __init__(self, n, ope=min, ide=1 << 30):
        self.size = 1 << n.bit_length()
        self.data = [ide] * (self.size << 1)
        self.ope = ope
        self.ide = ide

    def __getitem__(self, i):
        return self.data[i + self.size]

    def update(self, i, x):
        i0 = i + self.size
        while i0:
            self.data[i0] = x
            x = self.ope(self.data[i0], self.data[i0 ^ 1])
            i0 >>= 1

    def range(self, i, j):
        x = self.ide
        i0 = i + self.size
        j0 = j + self.size
        while i0 < j0:
            if i0 & 1:
                x = self.ope(x, self.data[i0])
                i0 += 1
            if j0 & 1:
                x = self.ope(x, self.data[j0 - 1])
            i0 >>= 1
            j0 >>= 1
        return x


class LazySegmentTree:
    def __init__(self, n, ope=min, ide=2 ** 31 - 1):
        m = 2 ** (n - 1).bit_length()
        self.data = [ide] * (2 * m)
        self.memo = [None] * (2 * m)
        self.size = m
        self.ope = ope
        self.ide = ide

    def __getitem__(self, i):
        return self.data[i + self.size]

    def __covering_index(self, i, j):
        i0 = i + self.size
        flag = 0
        while i0 // 2:
            if i0 % 2:
                flag = 1
            if flag:
                yield i0 // 2
            i0 //= 2
        j0 = j + self.size
        flag = 0
        while j0 // 2:
            if j0 % 2:
                flag = 1
            if flag:
                yield j0 // 2
            j0 //= 2

    def __covered_index(self, i, j):
        i0 = i + self.size
        j0 = j + self.size
        while i0 < j0:
            if i0 % 2:
                yield i0
                i0 += 1
            if j0 % 2:
                yield j0 - 1
            i0 //= 2
            j0 //= 2

    def __lazy_update(self, k):
        if self.memo[k] is None:
            return
        if k < self.size:
            self.data[2 * k] = self.memo[k]
            self.memo[2 * k] = self.memo[k]
            self.data[2 * k + 1] = self.memo[k]
            self.memo[2 * k + 1] = self.memo[k]
        self.memo[k] = None

    def range_update(self, i, j, x):
        covering = [*self.__covering_index(i, j)]
        for k in covering[::-1]:
            self.__lazy_update(k)
        for k in self.__covered_index(i, j):
            self.memo[k] = x
            self.data[k] = x
        for k in covering:
            left = self.data[2 * k]
            right = self.data[2 * k + 1]
            self.data[k] = self.ope(left, right)

    def range_ope(self, i, j):
        for k in [*self.__covering_index(i, j)][::-1]:
            self.__lazy_update(k)
        x = self.ide
        for k in self.__covered_index(i, j):
            x = self.ope(x, self.data[k])
        return x
