from depth_first_search import DFS


def bridges(graph):
    n = len(graph)
    dfs = DFS(graph)
    order = [None] * n
    for i, x in enumerate(dfs.preorder):
        order[x] = i
    lower = order[:]
    for x in dfs.preorder[::-1]:
        for y in graph[x]:
            if y == dfs.parent[x]:
                continue
            lower[x] = min(lower[x], lower[y])
    for x in range(n):
        for y in graph[x]:
            if order[x] < lower[y]:
                yield x, y
