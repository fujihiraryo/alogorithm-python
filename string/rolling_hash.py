class HashString:
    def __init__(self, S, x, y, b=2, p=10 ** 9 + 7):
        self.S, self.x, self.y, self.b, self.p = S, x, y, b, p
        h = 0
        for i in range(x, y):
            h = (h * b + ord(S[i])) % p
        self.hash = h

    def pop_left(self):
        S, x, y, b, p, h = self.S, self.x, self.y, self.b, self.p, self.hash
        self.hash = (h - ord(S[x]) * pow(b, y - x - 1, p)) % p
        self.x += 1

    def pop_right(self):
        S, y, b, p, h = self.S, self.y, self.b, self.p, self.hash
        self.hash = ((h - ord(S[y - 1])) * pow(b, p - 2, p)) % p
        self.y -= 1

    def push_left(self):
        S, x, y, b, p, h = self.S, self.x, self.y, self.b, self.p, self.hash
        self.hash = (h + ord(S[x - 1]) * pow(b, y - x, p)) % p
        self.x -= 1

    def push_right(self):
        S, y, b, p, h = self.S, self.y, self.b, self.p, self.hash
        self.hash = (h * b + ord(S[y])) % p
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
    for i in range(n1 - n0 + 1):
        if hS0.hash == hS1.hash:
            return True
        try:
            hS1.shift_right()
        except BaseException:
            pass
    return False


def count(S0, S1):
    # S0がS1に現れる回数を数える
    n0, n1 = len(S0), len(S1)
    if n0 > n1:
        return 0
    hS0 = HashString(S0, 0, n0)
    hS1 = HashString(S1, 0, n0)
    cnt = 0
    for i in range(n1 - n0 + 1):
        if hS0.hash == hS1.hash:
            cnt += 1
        try:
            hS1.shift_right()
        except BaseException:
            pass
    return cnt
