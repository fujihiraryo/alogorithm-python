class UnionFind:
    def __init__(self, n):
        self.size = n
        self.parents = [i for i in range(n)]

    def find(self, i):
        tmp = i
        while self.parents[tmp] != tmp:
            tmp = self.parents[tmp]
        return tmp

    def unite(self, i, j):
        i0, j0 = self.find(i), self.find(j)
        if i0 > j0:
            i0, j0 = j0, i0
        self.parents[j0] = i0
