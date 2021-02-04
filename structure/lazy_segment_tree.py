class Monoid:
    def __init__(self, a, k):
        self.value = a
        self.size = k

    def __add__(self, other):
        value = self.value + other.value
        size = self.size + other.size
        return Monoid(value, size)


class Operator:
    def __init__(self, x):
        self.x = x

    def __call__(self, a):
        return (self.x * a[1] + a[0], a[1])

    def __mult__(self, other):
        return Operator(self.x + other.x)

    def __eq__(self, other):
        return self.x == other.x


class LazySegmentTree:
    def __init__(self, n, ide, ope):
        self.size = 1 << (n - 1).bit_length()
        self.data = [ide] * (self.size << 1)
        self.memo = [ope] * (self.size << 1)
        self.ide = ide

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
            i0 //= 2
            j0 //= 2
        i0 = i + self.size
        j0 = j + self.size
        while i0 < j0:
            if i0 % 2:
                i0 += 1
            if j0 % 2:
                yield j0 - 1
            i0 //= 2
            j0 //= 2

    def __lazy_update(self, k):
        if self.memo[k] == self.ope:
            return
        if k < self.size:
            self.data[2 * k] = self.memo[k](self.data[2 * k])
            self.memo[2 * k] = self.memo[k] * self.memo[2 * k]
            self.data[2 * k + 1] = self.memo[k](self.data[2 * k + 1])
            self.memo[2 * k + 1] = self.memo[k] * self.memo[2 * k + 1]
        self.memo[k] = self.ope

    def range_update(self, i, j, ope):
        for k in [*self.__covering_index(i, j)][::-1]:
            self.__lazy_update(k)
        for k in self.__covered_index(i, j):
            self.memo[k] = ope * self.memo[k]
            self.data[k] = ope(self.data[k])
        for k in self.__covering_index(i, j):
            left = self.data[2 * k]
            right = self.data[2 * k + 1]
            self.data[k] = left + right

    def range_ope(self, i, j):
        for k in [*self.__covering_index(i, j)][::-1]:
            self.__lazy_update(k)
        x = self.ide
        for k in self.__covered_index(i, j):
            x = x + self.data[k]
        return x.value
