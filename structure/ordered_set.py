class OrderedSet:
    def __init__(self, n):
        d = 1
        while d ** 2 < n:
            d += 1
        self.size = d
        self.array = [[] for _ in range(d)]

    def __getitem__(self, k):
        cnt = 0
        for i in range(self.size):
            if k < cnt + len(self.array[i]):
                break
            cnt += len(self.array[i])
        return self.array[i][k - cnt]

    def __getblock(self, x):
        for i in range(self.size):
            if x < (i + 1) * self.size:
                break
        return i

    def index(self, x):
        i = self.__getblock(x)
        if x in self.array[i]:
            return self.array[i].index(x)
        return None

    def add(self, x):
        i = self.__getblock(x)
        if x in self.array[i]:
            return
        for j in range(len(self.array[i])):
            if x < self.array[i][j]:
                self.array[i].insert(j, x)
                return
        self.array[i].append(x)

    def remove(self, x):
        i = self.__getblock(x)
        if x in self.array[i]:
            self.array[i].remove(x)
