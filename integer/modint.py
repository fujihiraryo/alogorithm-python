class Mint:
    def __init__(self, val, MOD=10 ** 9 + 7):
        self.val = val % MOD
        self.MOD = MOD

    def __repr__(self):
        return str(self.val)

    def __eq__(self, other):
        return self.val == other.val

    def __add__(self, other):
        return Mint((self.val + other.val) % self.MOD)

    def __sub__(self, other):
        return Mint((self.val - other.val) % self.MOD)

    def __mul__(self, other):
        return Mint((self.val * other.val) % self.MOD)

    def __truediv__(self, other):
        return self.__mul__(other.__inv__())

    def __pow__(self, p):
        return Mint(pow(self.val, p, self.MOD))

    def __inv__(self):
        return Mint(pow(self.val, self.MOD - 2, self.MOD))
