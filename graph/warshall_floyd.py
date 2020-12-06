def warshall_floyd(graph):
    INF = 1 << 30
    n = len(graph)
    dist = [[INF for i in range(n)] for j in range(n)]
    for i in range(n):
        dist[i][i] = 0
        for j in graph[i].keys():
            dist[i][j] = graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
