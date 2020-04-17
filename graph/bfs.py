from collections import deque


def bfs(G, a, b):
    # グラフGにおいてaからbへの距離
    # 到達不可能な場合は-1を返す
    n = len(G)
    D = [-1] * n
    Q = deque([a])
    D[a] = 0
    while Q:
        x = Q.popleft()
        if x == b:
            return D[b]
        for y in G[x]:
            if D[y] == -1:
                Q.append(y)
                D[y] = D[x] + 1
    return D[b]


# テスト
G = [[3], [2], [1], [0, 4], [3]]
print(bfs(G, 0, 4))
print(bfs(G, 0, 1))
