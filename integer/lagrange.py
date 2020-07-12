class Lagrange:
    def __init__(self, lst):
        self.lst = lst

    def f(self, j, x):
        prd = 1
        for i, (xi, yi) in enumerate(self.lst):
            if j != i:
                prd *= (x - xi)
        return prd

    def P(self, x):
        tmp = 0
        for i, (xi, yi) in enumerate(self.lst):
            tmp += yi * (self.f(i, x) // self.f(i, xi))
        return tmp


if __name__ == "__main__":
    # P(x)=x**2-3*x+10
    lst = [(0, 10), (1, 8), (2, 8), (3, 10)]
    lag = Lagrange(lst)
    for i in range(10):
        print(lag.P(i))
