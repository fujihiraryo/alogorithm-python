import heapq
from collections import defaultdict


class PriorityQuene:
    def __init__(self):
        self.heap = []
        self.count = defaultdict(int)

    def push(self, x):
        heapq.heappush(self.heap, x)
        self.count[x] += 1

    def pop(self):
        return heapq.heappop(self.heap)

    def top(self):
        return self.heap[0]

    def remove(self, x):
        if self.count[x] == 0:
            return
        self.count[x] -= 1
        while self.heap:
            if self.count[self.heap[0]]:
                break
            heapq.heappop(self.heap)
