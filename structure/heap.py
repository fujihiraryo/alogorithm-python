class Heap():
    def __init__(self, A, reverse=False):
        if reverse:
            self.sgn = -1
            self.A = sorted([-a for a in A])
        else:
            self.sgn = 1
            self.A = sorted(A)

    def push(self, x):
        i = len(self.A)
        self.A.append(x*self.sgn)
        while i > 0:
            p = (i-1)//2
            if self.A[p] <= x*self.sgn:
                break
            self.A[i], self.A[p] = self.A[p], self.A[i]
            i = p

    def pop(self):
        x = self.A[0]
        y = self.A[-1]
        i = 0
        while 2*i+1 < len(self.A):
            a, b = 2*i+1, 2*i+2
            if b < len(self.A) and self.A[b] < self.A[a]:
                a = b
            if self.A[a] >= y:
                break
            self.A[i] = self.A[a]
            i = a
        self.A[i] = y
        self.A.pop()
        return x*self.sgn

    def top(self):
        return self.A[0]*self.sgn


# テスト
Q = [3, 5, 2, 4]
HQ = Heap(Q, reverse=True)
print(HQ.A)
HQ.push(6)
print(HQ.top())
