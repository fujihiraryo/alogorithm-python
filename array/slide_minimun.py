from collections import deque


def slide_min(a, k):
    n = len(a)
    deq = deque()
    b = []
    for i in range(n):
        while deq and a[deq[-1]] >= a[i]:
            deq.pop()
        deq.append(i)
        if i >= k - 1:
            b.append(a[deq[0]])
        if deq[0] == i - 2:
            deq.popleft()
    return b
