from collections import deque


class Tree():
    def __init__(self, G, r):
        # グラフGと根rから、各ノードの親ノードを求める
        n = len(G)
        P = [None for i in range(n)]
        V = [False for i in range(n)]
        que = deque([r])
        while que:
            x = que.popleft()
            V[x] = True
            for y in G[x]:
                if not V[y]:
                    P[y] = x
                    que.append(y)
        self.P = P


# テスト
G = [[4], [4], [3], [2, 5], [0, 1, 5], [3, 4]]
tree = Tree(G, 5)
print(tree.P)
tree = Tree(G, 1)
print(tree.P)
