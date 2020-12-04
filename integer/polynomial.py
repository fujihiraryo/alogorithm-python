class Polynomial:
    def __init__(self, coefficients, zero=0):
        self.coefficients = coefficients
        self.zero = zero

    def substitute(self, x):
        y = self.zero
        for i, a in enumerate(self.coefficients):
            y = y + a * x ** i
        return y

    def __mul__(self, polynomial):
        m = len(self.coefficients)
        n = len(polynomial.coefficients)
        coefficients = [self.zero] * (m + n - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(polynomial.coefficients):
                coefficients[i + j] = coefficients[i + j] + a * b
        return Polynomial(coefficients)

    def antiderivative(self):
        coefficients = [self.zero] * (len(self.coefficients) + 1)
        for i, a in enumerate(self.coefficients):
            coefficients[i + 1] = a / (i + 1)
        return Polynomial(coefficients)

    def integrate(self, a, b):
        P = self.antiderivative()
        return P.substitute(b) - P.substitute(a)
