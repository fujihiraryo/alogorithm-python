def breadth_first_search(graph, start, goal):
    dist = [-1] * len(graph)
    dist[start] = 0
    queue = [start]
    for x in queue:
        if x == goal:
            break
        for y in graph[x]:
            if dist[y] == -1:
                queue.append(y)
                dist[y] = dist[x] + 1
    return dist[goal]
