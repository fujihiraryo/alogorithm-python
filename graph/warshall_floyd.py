INF = 1 << 30


def warshall_floyd(graph):
    n = len(graph)
    dist = [[INF] * n for _ in range(n)]
    for x in range(n):
        dist[x][x] = 0
        for y in graph[x]:
            dist[x][y] = graph[x][y]
    for z in range(n):
        for x in range(n):
            for y in range(n):
                dist[x][y] = min(dist[x][y], dist[x][z] + dist[z][y])
    return dist
