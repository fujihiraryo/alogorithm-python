class HLD:
    def __init__(self, tree, root=0):
        n = len(tree)
        parent = [root] * n
        children = [[] for _ in range(n)]
        order = []
        queue = [root]
        for x in queue:
            order.append(x)
            for y in tree[x]:
                if y == parent[x]:
                    continue
                parent[y] = x
                children[x].append(y)
                queue.append(y)
        size = [1] * n
        for x in order[::-1]:
            for y in children[x]:
                size[x] += size[y]
        group = [-1] * n
        index = [-1] * n
        time = 0
        for x in order:
            if index[x] != -1:
                continue
            leader = x
            while True:
                group[x] = leader
                index[x] = time
                time += 1
                if size[x] == 1:
                    break
                x = max(children[x], key=lambda i: size[i])
        self.parent = parent
        self.group = group
        self.index = index
