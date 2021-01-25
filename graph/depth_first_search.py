from dataclasses import dataclass


@dataclass
class Forest:
    discovered: list
    finished: list
    parent: list
    children: list


def dfs(graph):
    n = len(graph)
    discovered = [-1] * n
    finished = [-1] * n
    parent = [-1] * n
    children = [[] for _ in range(n)]
    time = 0
    for i in range(n):
        if discovered[i] != -1:
            continue
        stack = [(i, -1)]
        while stack:
            x, p = stack[-1]
            if discovered[x] == -1:
                discovered[x] = time
                parent[x] = p
                children[p].append(x)
                time += 1
            stop = 1
            for y in graph[x]:
                if discovered[y] != -1:
                    continue
                stop = 0
                stack.append((y, x))
                break
            if stop:
                stack.pop()
                finished[x] = time
                time += 1
    return Forest(discovered, finished, parent, children)


graph = [[4, 7], [2, 3], [1, 3], [0, 4], [5], [7], [5], [6]]
forest = dfs(graph)
print(forest.discovered)
print(forest.finished)
print(forest.parent)
print(forest.children)
