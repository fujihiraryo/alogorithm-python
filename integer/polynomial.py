class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def substitute(self, x):
        y = 0
        for i, a in enumerate(self.coefficients):
            y = y + a * x ** i
        return y

    def __mul__(self, other):
        m = len(self.coefficients)
        n = len(other.coefficients)
        coefficients = [0] * (m + n - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                coefficients[i + j] = coefficients[i + j] + a * b
        return Polynomial(coefficients)

    def antiderivative(self):
        coefficients = [0] * (len(self.coefficients) + 1)
        for i, a in enumerate(self.coefficients):
            coefficients[i + 1] = a / (i + 1)
        return Polynomial(coefficients)

    def integrate(self, a, b):
        p = self.antiderivative()
        return p.substitute(b) - p.substitute(a)
