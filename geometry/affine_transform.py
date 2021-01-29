class Affine:
    def __init__(self, mat=((1, 0, 0), (0, 1, 0), (0, 0, 1))):
        self.mat = mat

    def __call__(self, x):
        x1 = (x[0], x[1], 1)
        y1 = [0] * 3
        for i in range(3):
            for j in range(3):
                y1[i] += self.mat[i][j] * x1[j]
        return y1[:2]

    def __mul__(self, other):
        a = self.mat
        b = other.mat
        c = [[0] * 3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    c[i][j] += a[i][k] * b[k][j]
        return Affine(c)


# example
expand = lambda sx, sy: Affine(((sx, 0, 0), (0, sy, 0), (0, 0, 1)))
rotate90 = Affine(((0, -1, 0), (1, 0, 0), (0, 0, 1)))
parallel = lambda x, y: Affine(((1, 0, x), (0, 1, y), (0, 0, 1)))
mirror_x = lambda p: Affine(((-1, 0, 2 * p), (0, 1, 0), (0, 0, 1)))
mirror_y = lambda p: Affine(((1, 0, 0), (0, -1, 2 * p), (0, 0, 1)))
