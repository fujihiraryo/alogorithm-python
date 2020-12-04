def bfs(graph, a, b):
    n = len(graph)
    dist = [-1] * n
    queue = [a]
    dist[a] = 0
    for x in queue:
        if x == b:
            return dist[b]
        for y in graph[x]:
            if dist[y] == -1:
                queue.append(y)
                dist[y] = dist[x] + 1
    return dist[b]
