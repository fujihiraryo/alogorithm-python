class SparseTable:
    def __init__(self, a):
        n = len(a)
        table = [[a[i]] for i in range(n)]
        for k in range(n.bit_length()):
            for i in range(n):
                if i + 2 ** (k + 1) > n:
                    continue
                x = table[i][k]
                y = table[i + 2 ** k][k]
                table[i].append(min(x, y))
        self.table = table
        self.bit_length = [i.bit_length() for i in range(n + 1)]

    def range(self, i, j):
        k = self.bit_length[j - i] - 1
        return min(self.table[i][k], self.table[j - 2 ** k][k])
