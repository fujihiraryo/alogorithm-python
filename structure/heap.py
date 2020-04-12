class Heap(list):
    def push(self, x):
        i = len(self)
        print(i)
        self.append(x)
        while i > 0:
            p = (i-1)//2
            if self[p] <= x:
                break
            self[i], self[p] = self[p], self[i]
            i = p

    def hpop(self):
        x = self[0]
        y = self[-1]
        i = 0
        while 2*i+1 < len(self):
            a, b = 2*i+1, 2*i+2
            if b < len(self) and self[b] < self[a]:
                a = b
            if self[a] >= y:
                break
            self[i] = self[a]
            i = a
        self[i] = y
        self.pop()
        return x

    def top(self):
        return self[0]


# テスト
Q = [2, 3, 4, 5]
HQ = Heap(Q)
print(HQ.hpop())
HQ.push(1)
print(HQ.top())
