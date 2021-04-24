class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j):
        i, j = self.find(i), self.find(j)
        if i == j:
            return
        if i > j:
            i, j = j, i
        self.parent[j] = i
        self.count -= 1

    def same(self, i, j):
        return self.find(i) == self.find(j)


class WeightedUnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.weight = [0] * n

    def find(self, i):
        j = i
        while self.parent[j] != j:
            j = self.parent[j]
            self.parent[i] = j
            self.weight[i] += self.weight[j]
        return j

    def diff(self, i, j):
        if self.find(i) != self.find(j):
            return None
        return self.weight[j] - self.weight[i]

    def unite(self, i, j, w):
        i0, j0 = self.find(i), self.find(j)
        w0 = w + self.weight[i] - self.weight[j]
        if i0 == j0:
            return
        if i0 > j0:
            i0, j0 = j0, i0
            w0 = -w0
        self.parent[j0] = i0
        self.weight[j0] = w0
