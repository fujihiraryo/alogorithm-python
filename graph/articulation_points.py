def articulation_points(graph):
    # depth first search
    n = len(graph)
    parent = [None] * n
    children = [[] for _ in range(n)]
    lst = []
    stack = [(None, 0)]
    visited = [0] * n
    while stack:
        p, x = stack.pop()
        if visited[x]:
            continue
        visited[x] = 1
        parent[x] = p
        if p is not None:
            children[p].append(x)
        lst.append(x)
        for y in graph[x]:
            if visited[y]:
                continue
            stack.append((x, y))
    # lowlink
    order = [None] * n
    lower = [None] * n
    for i, x in enumerate(lst):
        order[x] = i
        lower[x] = i
    for x in lst[::-1]:
        for y in graph[x]:
            if y == parent[x]:
                continue
            lower[x] = min(lower[x], lower[y])
    # result
    res = []
    if len(children[0]) > 1:
        res.append(0)
    for x in range(1, n):
        if any(order[x] <= lower[y] for y in children[x]):
            res.append(x)
    return res
