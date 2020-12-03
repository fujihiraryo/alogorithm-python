import heapq


def dijkstra(G, r):
    # rを始点とする各点へのパスの長さを求める
    n = len(G)
    inf = 10 ** 20
    D = [inf for i in range(n)]
    D[r] = 0
    Q = [(0, r)]
    heapq.heapify(Q)
    while Q:
        _, x = heapq.heappop(Q)
        for y in G[x].keys():
            if D[x] + G[x][y] < D[y]:
                D[y] = D[x] + G[x][y]
                heapq.heappush(Q, (D[y], y))
    return D
