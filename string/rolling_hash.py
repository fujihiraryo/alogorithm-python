class HashString:
    def __init__(self, S, l, r, b=2, p=10**9+7):
        self.S, self.l, self.r, self.b, self.p = S, l, r, b, p
        h = 0
        for i in range(l, r):
            h = (h*b+ord(S[i])) % p
        self.hash = h

    def pop_left(self):
        S, l, r, b, p, h = self.S, self.l, self.r, self.b, self.p, self.hash
        self.hash = (h-ord(S[l])*pow(b, r-l-1, p)) % p
        self.l += 1

    def pop_right(self):
        S, l, r, b, p, h = self.S, self.l, self.r, self.b, self.p, self.hash
        self.hash = ((h-ord(S[r-1])) * pow(b, p-2, p)) % p
        self.r -= 1

    def push_left(self):
        S, l, r, b, p, h = self.S, self.l, self.r, self.b, self.p, self.hash
        self.hash = (h+ord(S[l-1])*pow(b, r-l, p)) % p
        self.l -= 1

    def push_right(self):
        S, l, r, b, p, h = self.S, self.l, self.r, self.b, self.p, self.hash
        self.hash = (h*b+ord(S[r])) % p
        self.r += 1

    def shift_left(self):
        self.push_left()
        self.pop_right()

    def shift_right(self):
        self.push_right()
        self.pop_left()


def contain(S0, S1):
    # S0がS1に含まれるか判定する
    n0, n1 = len(S0), len(S1)
    if n0 > n1:
        return False
    hS0 = HashString(S0, 0, n0)
    hS1 = HashString(S1, 0, n0)
    if hS0.hash == hS1.hash:
        return True
    for i in range(n1-n0):
        hS1.shift_right()
        if hS0.hash == hS1.hash:
            return True
    return False


S = 'abcde'
hS = HashString(S, 1, 2)
print(hS.hash)
hS.push_right()
print(hS.hash)
hS.pop_right()
print(hS.hash)
hS.push_left()
print(hS.hash)
hS.pop_left()
print(hS.hash)
print(hS.r-hS.l)

S0 = 'abcd'
S1 = 'xxxabcdxx'
print(contain(S0, S1))

S0 = 'abcde'
S1 = 'xxxxabcdxeeee'
print(contain(S0, S1))
