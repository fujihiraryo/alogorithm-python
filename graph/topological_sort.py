def topological_sort(dag):
    n = len(dag)
    src = [set() for _ in range(n)]
    tgt = [set() for _ in range(n)]
    stack = set(range(n))
    for x in range(n):
        for y in dag[x]:
            src[y].add(x)
            tgt[x].add(y)
            if y in stack:
                stack.remove(y)
    while stack:
        x = stack.pop()
        yield x
        while tgt[x]:
            y = tgt[x].pop()
            src[y].remove(x)
            if src[y]:
                continue
            stack.add(y)
