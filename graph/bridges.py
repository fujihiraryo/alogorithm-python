def bridges(graph):
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
    for x in range(n):
        for y in graph[x]:
            if order[x] < lower[y]:
                res.append(sorted((x, y)))
    return res


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
ans = bridges(graph)
for x in sorted(ans):
    print(*x)
