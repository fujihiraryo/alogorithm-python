class SegmentTree:
    def __init__(self, n, ide):
        self.size = 1 << n.bit_length()
        self.data = [ide] * (self.size << 1)
        self.ide = ide

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

    def update(self, i, ope):
        i0 = i + self.size
        self.data[i0] = ope(self.data[i0])
        while i0:
            i0 >>= 1
            left = self.data[2 * i0]
            right = self.data[2 * i0 + 1]
            self.data[i0] = left + right

    def range_merge(self, i, j):
        x = self.ide
        for k in self.__covered_index(i, j):
            x = x + self.data[k]
        return x.value


class Monoid:
    # example(RSQ)
    def __init__(self, value, length):
        self.value = value
        self.length = length

    def __add__(self, other):
        value = self.value + other.value
        length = self.length + other.length
        return Monoid(value, length)


class Operator:
    # example(RAQ)
    def __init__(self, x):
        self.x = x

    def __call__(self, monoid):
        return Monoid(self.x * monoid.length + monoid.value, monoid.length)
