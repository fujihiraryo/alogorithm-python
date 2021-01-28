class SegmentTree:
    def __init__(self, n, op=min, ide=1 << 30):
        self.size = 1 << n.bit_length()
        self.tree = [ide] * (self.size << 1)
        self.op = op
        self.ide = ide

    def __getitem__(self, i):
        return self.tree[i + self.size]

    def update(self, i, x):
        i0 = i + self.size
        while i0:
            self.tree[i0] = x
            x = self.op(self.tree[i0], self.tree[i0 ^ 1])
            i0 >>= 1

    def range(self, i, j):
        x = self.ide
        i0 = i + self.size
        j0 = j + self.size
        while i0 < j0:
            if i0 & 1:
                x = self.op(x, self.tree[i0])
                i0 += 1
            if j0 & 1:
                x = self.op(x, self.tree[j0 - 1])
            i0 >>= 1
            j0 >>= 1
        return x
