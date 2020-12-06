INF = 1 << 30


def maximum_flow(graph, start, goal):
    n = len(graph)
    max_flow = 0
    while True:
        # find path
        visited = [0] * n
        stack = [start]
        last = [None] * n
        while stack:
            x = stack.pop()
            visited[x] = 1
            if x == goal:
                break
            for y in graph[x].keys():
                if visited[y] or graph[x][y] == 0:
                    continue
                stack.append(y)
                last[y] = x
        if x != goal:
            break
        # min capacity
        y = goal
        min_capacity = INF
        while last[y] is not None:
            x = last[y]
            min_capacity = min(min_capacity, graph[x][y])
            y = x
        # update graph
        y = goal
        while last[y] is not None:
            x = last[y]
            graph[x][y] -= min_capacity
            graph[y][x] += min_capacity
            y = x
        max_flow += min_capacity
    return max_flow
