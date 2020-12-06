def depth_first_search(graph, start, goal):
    visited = [0] * len(graph)
    stack = [start]
    while stack:
        x = stack.pop()
        if x == goal:
            return True
        visited[x] = 1
        for y in graph[x]:
            if visited[y]:
                continue
            stack.append(y)
    return False
