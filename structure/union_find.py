class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def unite(self, i, j):
        i0, j0 = self.find(i), self.find(j)
        if i0 > j0:
            i0, j0 = j0, i0
        self.parent[j0] = i0
