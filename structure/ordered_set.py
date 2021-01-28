class OrderedSet:
    # 長さnでn未満の要素からなる整列集合
    def __init__(self, n):
        d = 1
        while d ** 2 < n:
            d += 1
        self.size = d
        self.bucket = [[] for _ in range(d)]

    def __getitem__(self, k):
        cnt = 0
        for i in range(self.size):
            if k < cnt + len(self.bucket[i]):
                break
            cnt += len(self.bucket[i])
        return self.bucket[i][k - cnt]

    def __bucketindex(self, x):
        for i in range(self.size):
            if x < (i + 1) * self.size:
                return i

    def index(self, x):
        i = self.__bucketindex(x)
        k = sum(len(self.bucket[j]) for j in range(i))
        if x not in self.bucket[i]:
            return None
        k += self.bucket[i].index(x)
        return k

    def add(self, x):
        i = self.__bucketindex(x)
        if x in self.bucket[i]:
            return
        for j in range(len(self.bucket[i])):
            if x < self.bucket[i][j]:
                self.bucket[i].insert(j, x)
                return
        self.bucket[i].append(x)

    def remove(self, x):
        i = self.__bucketindex(x)
        if x in self.bucket[i]:
            self.bucket[i].remove(x)
