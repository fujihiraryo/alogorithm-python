import heapq

INF = 1 << 30


def dijkstra(graph, start):
    dist = [INF] * len(graph)
    dist[start] = 0
    heap = [(0, start)]
    heapq.heapify(heap)
    while heap:
        _, x = heapq.heappop(heap)
        for y in graph[x]:
            if dist[y] > dist[x] + graph[x][y]:
                dist[y] = dist[x] + graph[x][y]
                heapq.heappush(heap, (dist[y], y))
    return dist
