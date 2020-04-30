class UnionFind():
    def __init__(self, n):
        self.n = n
        # 親の名(いない場合はNone)
        self.parent = [None] * n
        # 子の数
        self.count = [0] * n

    def root(self, x):
        # xの根を返す
        if self.parent[x] is None:
            return x
        else:
            return self.root(self.parent[x])

    def union(self, x, y):
        # xとyをまとめる
        x0 = self.root(x)
        y0 = self.root(y)
        if x0 == y0:
            return
        if x0 > y0:
            x0, y0 = y0, x0
        self.parent[y0] = x0
        self.count[x0] += self.count[y0] + 1

    def size(self, x):
        # xの属する木の大きさ
        return self.count[self.root(x)] + 1

    def same(self, x, y):
        return self.root(x) == self.root(y)


# テスト
uf = UnionFind(5)
uf.union(0, 1)
uf.union(0, 2)
uf.union(3, 4)
print(uf.same(1, 2))
print(uf.same(1, 3))
