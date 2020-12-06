def topological_sort(graph):
    n = len(graph)
    in_set_list = [set() for _ in range(n)]
    out_set_list = [set() for _ in range(n)]
    stack_set = set(range(n))
    for x in range(n):
        for y in graph[x]:
            in_set_list[y].add(x)
            out_set_list[x].add(y)
            if y in stack_set:
                stack_set.remove(y)
    res = []
    while stack_set:
        x = stack_set.pop()
        res.append(x)
        while out_set_list[x]:
            y = out_set_list[x].pop()
            in_set_list[y].remove(x)
            if in_set_list[y]:
                continue
            stack_set.add(y)
    if any(out_set_list[x] for x in range(n)):
        return -1
    return res
