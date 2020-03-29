def dfs(G, a, b):
    # グラフGにおいてaからbに到達可能か
    n = len(G)
    visited = [False] * n
    que = [a]
    visited[a] = True
    while que:
        x = que.pop()
        if x == b:
            return True
        next = G[x]
        for y in next:
            if not visited[y]:
                que.append(y)
                visited[y] = True
    return False


# テスト
G = [[3, 4], [2], [1], [0, 4], [0, 3]]
print(dfs(G, 0, 4))
print(dfs(G, 0, 1))
