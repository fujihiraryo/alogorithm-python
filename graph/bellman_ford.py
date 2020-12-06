INF = 1 << 30


def bellman_ford(graph, start):
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    update = True
    cnt = 0
    while update:
        update = False
        cnt += 1
        if cnt > n:
            # 負の閉路を検出
            return -1
        for x in range(n):
            for y in graph[x].keys():
                if dist[x] != INF and dist[y] > dist[x] + graph[x][y]:
                    dist[y] = dist[x] + graph[x][y]
                    update = True
    return dist
