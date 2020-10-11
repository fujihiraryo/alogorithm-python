class Polynomial:
    def __init__(self, coefficients=[1], MOD=10 ** 9 + 7):
        self.coefficients = coefficients
        self.MOD = MOD

    def substitute(self, x):
        y = 0
        for i, a in enumerate(self.coefficients):
            y += a * x ** i
            y %= self.MOD
        return y

    def __mul__(self, polynomial):
        m = len(self.coefficients)
        n = len(polynomial.coefficients)
        coefficients = [0] * (m + n - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(polynomial.coefficients):
                coefficients[i + j] += a * b
                coefficients[i + j] %= self.MOD
        return Polynomial(coefficients)

    def antiderivative(self):
        coefficients = [0] * (len(self.coefficients) + 1)
        for i, a in enumerate(self.coefficients):
            coefficients[i + 1] = a * pow(i + 1, self.MOD - 2, self.MOD)
            coefficients[i + 1] %= self.MOD
        return Polynomial(coefficients)

    def integrate(self, a, b):
        P = self.antiderivative()
        return (P.substitute(b) - P.substitute(a)) % self.MOD


if __name__ == "__main__":
    p = Polynomial([1, 1, 1])
    print(p.substitute(2))
    print(p.integrate(0, 6))
