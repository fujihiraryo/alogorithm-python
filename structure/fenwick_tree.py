class BIT:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * (n + 1)

    def __getitem__(self, i):
        return self.sum(i + 1) - self.sum(i)

    def sum(self, i):
        s = 0
        tmp = i
        while tmp:
            s += self.arr[tmp]
            tmp -= tmp & -tmp
        return s

    def add(self, i, x):
        tmp = i + 1
        while tmp <= self.size:
            self.arr[tmp] += x
            tmp += tmp & -tmp


class RangeBIT:
    def __init__(self, n):
        self.bit0 = BIT(n)
        self.bit1 = BIT(n)

    def add(self, i, j, x):
        self.bit0.add(i, -x * i)
        self.bit0.add(j, x * j)
        self.bit1.add(i, x)
        self.bit1.add(j, -x)

    def sum(self, i, j):
        si = self.bit0.sum(i) + self.bit1.sum(i) * i
        sj = self.bit0.sum(j) + self.bit1.sum(j) * j
        return sj - si
