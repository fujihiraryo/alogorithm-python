from depth_first_search import DFS


def articulation_points(graph):
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
    if len(dfs.children[0]) > 1:
        yield 0
    for x in range(1, n):
        if any(order[x] <= lower[y] for y in dfs.children[x]):
            yield x
