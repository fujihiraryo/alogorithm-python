def scc(graph):
    n = len(graph)
    # dfs
    checked = [0] * n
    lst = []
    for i in range(n):
        if checked[i]:
            continue
        stack = [i]
        checked[i] = 1
        while stack:
            x = stack[-1]
            stop = 1
            for y in graph[x]:
                if checked[y]:
                    continue
                checked[y] = 1
                stack.append(y)
                stop = 0
                break
            if stop:
                lst.append(x)
                stack.pop()
    # reverse
    reverse = [set() for _ in range(n)]
    for x in range(n):
        for y in graph[x]:
            reverse[y].add(x)
    # dfs
    visited = [0] * n
    cnt = 0
    group = [-1] * n
    for i in lst[::-1]:
        if visited[i]:
            continue
        stack = [i]
        group[i] = cnt
        while stack:
            x = stack.pop()
            visited[x] = 1
            for y in reverse[x]:
                if visited[y]:
                    continue
                group[y] = cnt
                stack.append(y)
        cnt += 1
    return group
