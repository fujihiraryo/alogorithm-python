from depth_first_search import DFS


def scc(graph):
    n = len(graph)
    dfs = DFS(graph)
    order = dfs.postorder[::-1]
    index = [None] * n
    for i, x in enumerate(order):
        index[x] = i
    reverse = [set() for _ in range(n)]
    for x in range(n):
        for y in graph[x]:
            reverse[index[y]].add(index[x])
    dfs = DFS(reverse)
    group = [None] * n
    cnt = -1
    for i in dfs.preorder:
        if dfs.parent[i] == -1:
            cnt += 1
        group[order[i]] = cnt
    return group
