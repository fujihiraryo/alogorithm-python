from collections import deque


def bfs(G, a, b):
    # グラフGにおいてaからbへの距離
    # 到達不可能な場合は-1を返す
    n = len(G)
    d = [-1] * n
    que = deque([a])
    d[a] = 0
    while que:
        x = que.popleft()
        if x == b:
            return d[b]
        next = G[x]
        for y in next:
            if d[y] == -1:
                que.append(y)
                d[y] = d[x] + 1
    return d[b]


# テスト
G = [[3], [2], [1], [0, 4], [3]]
print(bfs(G, 0, 4))
print(bfs(G, 0, 1))
