import sys

sys.setrecursionlimit(10 ** 7)


class DFS:
    def __init__(self, graph):
        n = len(graph)
        self.graph = graph
        self.visited = [0] * n
        self.preorder = []
        self.postorder = []
        self.parent = [-1] * n
        self.children = [[] for _ in range(n)]
        for i in range(n):
            if self.visited[i]:
                continue
            self.visit(i)

    def visit(self, x):
        self.visited[x] = 1
        self.preorder.append(x)
        for y in self.graph[x]:
            if self.visited[y]:
                continue
            self.parent[y] = x
            self.children[x].append(y)
            self.visit(y)
        self.postorder.append(x)
