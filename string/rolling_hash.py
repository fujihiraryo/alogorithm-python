class HashString:
    def __init__(self, s, x, y, b=2, p=10 ** 9 + 7):
        self.s, self.x, self.y, self.b, self.p = s, x, y, b, p
        h = 0
        for i in range(x, y):
            h = (h * b + ord(s[i])) % p
        self.hash = h

    def pop_left(self):
        s, x, y, b, p, h = self.s, self.x, self.y, self.b, self.p, self.hash
        self.hash = (h - ord(s[x]) * pow(b, y - x - 1, p)) % p
        self.x += 1

    def pop_right(self):
        s, y, b, p, h = self.s, self.y, self.b, self.p, self.hash
        self.hash = ((h - ord(s[y - 1])) * pow(b, p - 2, p)) % p
        self.y -= 1

    def push_left(self):
        s, x, y, b, p, h = self.s, self.x, self.y, self.b, self.p, self.hash
        self.hash = (h + ord(s[x - 1]) * pow(b, y - x, p)) % p
        self.x -= 1

    def push_right(self):
        s, y, b, p, h = self.s, self.y, self.b, self.p, self.hash
        self.hash = (h * b + ord(s[y])) % p
        self.r += 1

    def shift_left(self):
        self.push_left()
        self.pop_right()

    def shift_right(self):
        self.push_right()
        self.pop_left()


def contain(s0, s1):
    # s0がs1に含まれるか判定する
    n0, n1 = len(s0), len(s1)
    if n0 > n1:
        return False
    hs0 = HashString(s0, 0, n0)
    hs1 = HashString(s1, 0, n0)
    for i in range(n1 - n0 + 1):
        if hs0.hash == hs1.hash:
            return True
        try:
            hs1.shift_right()
        except BaseException:
            pass
    return False


def count(s0, s1):
    # s0がs1に現れる回数を数える
    n0, n1 = len(s0), len(s1)
    if n0 > n1:
        return 0
    hs0 = HashString(s0, 0, n0)
    hs1 = HashString(s1, 0, n0)
    cnt = 0
    for i in range(n1 - n0 + 1):
        if hs0.hash == hs1.hash:
            cnt += 1
        try:
            hs1.shift_right()
        except BaseException:
            pass
    return cnt
