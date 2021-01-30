class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.group_size = [1] * n

    def find(self, i):
        j = i
        while self.parent[j] != j:
            j = self.parent[j]
            self.parent[i] = j
        return j

    def unite(self, i, j):
        i0, j0 = self.find(i), self.find(j)
        if i0 > j0:
            i0, j0 = j0, i0
        self.parent[j0] = i0
        if i0 != j0:
            self.group_size[i0] += self.group_size[j0]


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
