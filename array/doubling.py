class Doubling:
    def __init__(self, parent, root=0):
        n = len(parent)
        double = [parent]
        for i in range(n.bit_length()):
            lst = []
            for x in range(n):
                lst.append(double[i][double[i][x]])
            double.append(lst)
        self.double = double
        depth = []
        for x in range(n):
            d = 0
            y = x
            for i in range(len(self.double))[::-1]:
                if self.double[i][y] != root:
                    y = self.double[i][y]
                    d += 2 ** i
            depth.append(d)
        self.depth = depth

    def forward(self, x, i):
        y, j = x, i
        cnt = 0
        while j:
            if j % 2:
                y = self.double[cnt][y]
            j //= 2
            cnt += 1
        return y

    def lca(self, x, y):
        x0, y0 = x, y
        if self.depth[x0] > self.depth[y0]:
            x0, y0 = y0, x0
        y0 = self.forward(y0, self.depth[y0] - self.depth[x0])
        if x0 == y0:
            return x0
        for i in range(len(self.double))[::-1]:
            if self.double[i][x0] != self.double[i][y0]:
                x0, y0 = self.double[i][x0], self.double[i][y0]
        return self.double[0][x0]
