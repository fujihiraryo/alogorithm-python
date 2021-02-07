class Bucket:
    def __init__(self, a, ide, fold, apply):
        n = len(a)
        d = 1
        while d ** 2 <= n:
            d += 1
        self.size = d
        self.ide = ide
        self.fold = fold
        self.apply = apply
        self.data = a
        self.block = [ide] * d
        for i in range(d):
            self.block_update(i)

    def __block_update(self, i):
        d = self.size
        x = self.ide
        for y in self.data[i * d : i * d + d]:
            x = self.fold(x, y)
        self.block[i] = x

    def point_apply(self, i, f):
        d = self.size
        self.data[i] = self.apply(f, self.data[i])
        self.__block_update(i // d)

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


class LazyBucket:
    def __init__(self, a, ide, idf, fold, compose, apply):
        n = len(a)
        d = 1
        while d ** 2 <= n:
            d += 1
        self.size = d
        self.ide = ide
        self.idf = idf
        self.fold = fold
        self.compose = compose
        self.apply = apply
        self.data = [ide] * d ** 2
        self.data[:n] = a
        self.block = [ide] * d
        self.memo = [idf] * d
        for i in range(d):
            self.block_update(i)

    def block_update(self, k):
        d = self.size
        x = self.ide
        for y in self.data[k * d : (k + 1) * d]:
            x = self.fold(x, y)
        self.block[k] = x

    def lazy_update(self, k):
        d = self.size
        for i in range(k * d, (k + 1) * d):
            self.data[i] = self.apply(self.memo[k], self.data[i])
        self.memo[k] = self.idf

    def range_apply(self, i, j, f):
        d = self.size
        if i // d == j // d:
            self.lazy_update(i // d)
            for k in range(i, j):
                self.data[k] = self.apply(f, self.data[k])
            self.block_update(i // d)
            return
        self.lazy_update(i // d)
        for k in range(i, -(-i // d) * d):
            self.data[k] = self.apply(f, self.data[k])
        self.block_update(i // d)
        for k in range(-(-i // d), j // d):
            self.block[k] = self.apply(f, self.block[k])
            self.memo[k] = self.compose(f, self.memo[k])
        self.lazy_update(j // d)
        for k in range((j // d) * d, j):
            self.data[k] = self.apply(f, self.data[k])
        self.block_update(j // d)

    def range_fold(self, i, j):
        d = self.size
        x = self.ide
        if i // d == j // d:
            self.lazy_update(i // d)
            for y in self.data[i:j]:
                x = self.fold(x, y)
            return x
        self.lazy_update(i // d)
        for y in self.data[i : -(-i // d) * d]:
            x = self.fold(x, y)
        for y in self.block[-(-i // d) : j // d]:
            x = self.fold(x, y)
        self.lazy_update(j // d)
        for y in self.data[(j // d) * d : j]:
            x = self.fold(x, y)
        return x
