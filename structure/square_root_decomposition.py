class RMQ:
    def __init__(self, n, INF=2 ** 31 - 1):
        d = 1
        while d ** 2 <= n:
            d += 1
        self.size = d
        self.bucket = [[INF] * d for _ in range(d)]
        self.bucket_min = [INF] * d
        self.min = lambda x: min(x, default=INF)

    def update(self, k, x):
        d = self.size
        i, j = k // d, k % d
        self.bucket[i][j] = x
        self.bucket_min[i] = min(self.bucket[i])

    def range(self, k0, k1):
        d = self.size
        i0, j0 = k0 // d, k0 % d
        i1, j1 = k1 // d, k1 % d
        if i0 == i1:
            return min(self.bucket[i0][j0:j1])
        return min(
            self.min(self.bucket_min[i0 + 1 : i1]),
            self.min(self.bucket[i0][j0:d]),
            self.min(self.bucket[i1][0:j1]),
        )


class RUQRMQ:
    def __init__(self, n, INF=2 ** 31 - 1):
        d = 1
        while d ** 2 <= n:
            d += 1
        self.size = d
        self.bucket = [[INF] * d for _ in range(d)]
        self.bucket_min = [INF] * d
        self.min = lambda x: min(x, default=INF)
        self.lazy_memo = [None] * d

    def lazy_update(self, i):
        if self.lazy_memo[i] is None:
            return
        self.bucket[i] = [self.lazy_memo[i]] * self.size
        self.lazy_memo[i] = None

    def update(self, k0, k1, x):
        d = self.size
        i0, j0 = k0 // d, k0 % d
        i1, j1 = k1 // d, k1 % d
        self.lazy_update(i0)
        self.lazy_update(i1)
        if i0 == i1:
            self.bucket[i0][j0:j1] = [x] * (j1 - j0)
            self.bucket_min[i0] = min(self.bucket[i0])
            return
        self.bucket[i0][j0:d] = [x] * (d - j0)
        self.bucket_min[i0] = min(self.bucket[i0])
        self.lazy_memo[i0 + 1 : i1] = [x] * (i1 - i0 - 1)
        self.bucket_min[i0 + 1 : i1] = [x] * (i1 - i0 - 1)
        self.bucket[i1][0:j1] = [x] * j1
        self.bucket_min[i1] = min(self.bucket[i1])

    def range(self, k0, k1):
        d = self.size
        i0, j0 = k0 // d, k0 % d
        i1, j1 = k1 // d, k1 % d
        self.lazy_update(i0)
        self.lazy_update(i1)
        if i0 == i1:
            return min(self.bucket[i0][j0:j1])
        return min(
            self.min(self.bucket_min[i0 + 1 : i1]),
            self.min(self.bucket[i0][j0:d]),
            self.min(self.bucket[i1][0:j1]),
        )
