class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.group_size = [1] * size
        self.unite_count = [0] * size

    def find(self, i):
        j = i
        while self.parent[j] != j:
            j = self.parent[j]
        return j

    def unite(self, i, j):
        i0, j0 = self.find(i), self.find(j)
        if i0 > j0:
            i0, j0 = j0, i0
        self.unite_count[i0] += 1
        self.parent[j0] = i0
        if i0 != j0:
            self.unite_count[i0] += self.unite_count[j0]
            self.group_size[i0] += self.group_size[j0]
