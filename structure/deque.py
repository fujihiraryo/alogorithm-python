class Deque():
    def __init__(self, A, buffer=10**6):
        self.A = [None]*buffer+A+[None]*buffer
        self.l = buffer
        self.r = buffer+len(A)-1

    def push_left(self, x):
        self.l -= 1
        self.A[self.l] = x

    def push_right(self, x):
        self.r += 1
        self.A[self.r] = x

    def pop_left(self, x):
        self.l += 1
        return self.A[self.l-1]

    def pop_right(self, x):
        self.r -= 1
        return self.A[self.r+1]

    def change(self, i, x):
        self.A[i+self.l] = x

    def access(self, i):
        return self.A[i+self.l]

    def bisect_left(self, x):
        l, r = self.l-1, self.r
        while r-l > 1:
            c = (l+r)//2
            if self.A[c] < x:
                l = c
            else:
                r = c
        return r-self.l

    def bisect_right(self, x):
        l, r = self.l-1, self.r
        while r-l > 1:
            c = (l+r)//2
            if self.A[c] <= x:
                l = c
            else:
                r = c
        return r-self.l


A = [2, 2]
deque = Deque(A)
deque.push_left(1)
deque.push_right(3)
print(deque.access(2))
deque.change(2, 10)
print(deque.access(2))
print(deque.bisect_left(2))
print(deque.bisect_right(2))
