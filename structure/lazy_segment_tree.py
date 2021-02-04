class LazySegmentTree:
    def __init__(self, n, ide, ope):
        self.size = 1 << (n - 1).bit_length()
        self.data = [ide] * (self.size << 1)
        for k in range(1, self.size)[::-1]:
            self.data[k] = self.data[2 * k] + self.data[2 * k + 1]
        self.memo = [ope] * (self.size << 1)
        self.ide = ide
        self.ope = ope

    def __covering_index(self, i, j):
        i0 = i + self.size
        j0 = j + self.size
        i1 = (i0 // (i0 & -i0)) // 2
        j1 = (j0 // (j0 & -j0)) // 2
        while i0 < j0:
            if j0 <= j1:
                yield j0
            if i0 <= i1:
                yield i0
            i0 //= 2
            j0 //= 2
        while i0:
            yield i0
            i0 //= 2

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
            self.memo[2 * k] = self.memo[k] * self.memo[2 * k]
            self.data[2 * k] = self.memo[k](self.data[2 * k])
            self.memo[2 * k + 1] = self.memo[k] * self.memo[2 * k + 1]
            self.data[2 * k + 1] = self.memo[k](self.data[2 * k + 1])
        self.memo[k].__init__()

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

    def range_merge(self, i, j):
        for k in [*self.__covering_index(i, j)][::-1]:
            self.__lazy_update(k)
        x = self.ide
        for k in self.__covered_index(i, j):
            x = x + self.data[k]
        return x


class Monoid:
    # example(RSQ)
    def __init__(self, value=0, length=1):
        self.value = value
        self.length = length

    def __add__(self, other):
        value = self.value + other.value
        length = self.length + other.length
        return Monoid(value, length)


class Operator:
    # example(RUQ)
    def __init__(self, param=None):
        self.param = param

    def __call__(self, monoid):
        if self.param is None:
            return monoid
        value = self.param * monoid.length
        return Monoid(value, monoid.length)

    def __mul__(self, other):
        return Operator(self.param)

    def __eq__(self, other):
        return self.param == other.param


n, q = map(int, input().split())
a = LazySegmentTree(n, Monoid(), Operator())
for _ in range(q):
    cmd, *query = map(int, input().split())
    if cmd == 0:
        s, t, x = query
        a.range_update(s, t + 1, Operator(x))
    else:
        s, t = query
        print(a.range_merge(s, t + 1).value)
