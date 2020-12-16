def topological_sort(dag):
    n = len(dag)
    in_set_list = [set() for _ in range(n)]
    out_set_list = [set() for _ in range(n)]
    stack_set = set(range(n))
    for x in range(n):
        for y in dag[x]:
            in_set_list[y].add(x)
            out_set_list[x].add(y)
            if y in stack_set:
                stack_set.remove(y)
    while stack_set:
        x = stack_set.pop()
        yield x
        while out_set_list[x]:
            y = out_set_list[x].pop()
            in_set_list[y].remove(x)
            if in_set_list[y]:
                continue
            stack_set.add(y)
