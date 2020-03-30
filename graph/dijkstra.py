def dijkstra(G, s):
    # sを始点としてすべての点への最短距離を求める
    inf = 10**18
    n = len(G)
    d = [inf for i in range(n)]
    d[s] = 0
    que = list(range(n))
    while que:
        x = 0
        for y in que:
            if d[y] < d[x]:
                x = y
        x = que.pop(x)
        for y in G[x].keys():
            if d[y] > d[x]+G[x][y]:
                d[y] = d[x]+G[x][y]
    return d


# テスト
G = [{1: 5, 2: 1}, {0: 5, 2: 1}, {0: 1, 1: 1, 3: 10}, {2: 10}]
print(dijkstra(G, 0))
