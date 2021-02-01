import bisect


class RangeSearch:
    def __init__(self, x, y):
        n = len(x)
        d = 1
        while d ** 2 < n:
            d += 1
        idx = sorted(range(n), key=lambda i: x[i])
        sorted_x = sorted(x)
        sorted_y = [[] for _ in range(d)]
        bucket = [[] for _ in range(d)]
        for i in range(n):
            sorted_y[i // d].append(y[idx[i]])
            bucket[i // d].append(idx[i])
        for i in range(d):
            sorted_y[i].sort()
            bucket[i].sort(key=lambda i: y[i])
        self.x = x
        self.y = y
        self.sorted_x = sorted_x
        self.sorted_y = sorted_y
        self.bucket = bucket
        self.bucket_count = d

    def query(self, sx, tx, sy, ty):
        d = self.bucket_count
        ix = bisect.bisect_left(self.sorted_x[d - 1 :: d], sx)
        jx = bisect.bisect_right(self.sorted_x[0::d], tx)
        for i in range(ix, jx):
            iy = bisect.bisect_left(self.sorted_y[i], sy)
            jy = bisect.bisect_right(self.sorted_y[i], ty)
            for k in self.bucket[i][iy:jy]:
                if sx <= self.x[k] <= tx and sy <= self.y[k] <= ty:
                    yield k
