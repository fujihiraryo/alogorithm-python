class Bucket:
    def __init__(self, a, ide, fold, apply):
        n = len(a)
        d = 1
        while d ** 2 < n:
            d += 1
        self.size = d
        self.ide = ide
        self.fold = fold
        self.apply = apply
        self.data = a
        self.block = [ide] * d
        for i in range(d):
            self.block_update(i)

    def block_update(self, i):
        d = self.size
        x = self.ide
        for y in self.data[i * d : i * d + d]:
            x = self.fold(x, y)
        self.block[i] = x

    def point_apply(self, i, f):
        d = self.size
        self.data[i] = self.apply(f, self.data[i])
        self.block_update(i // d)

    def range_fold(self, i, j):
        d = self.size
        x = self.ide
        if i // d == j // d:
            for y in self.data[i:j]:
                x = self.fold(x, y)
            return x
        for y in self.data[i : -(-i // d) * d]:
            x = self.fold(x, y)
        for y in self.block[-(-i // d) : j // d]:
            x = self.fold(x, y)
        for y in self.data[(j // d) * d : j]:
            x = self.fold(x, y)
        return x
