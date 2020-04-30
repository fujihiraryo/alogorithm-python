def dfs(G, V, a, b):
    # グラフGにおいてaからbに到達可能か
    V[a] = True
    if a == b:
        return True
    for x in G[a]:
        if not V[x] and dfs(G, V, x, b):
            return True
    return False


# テスト
G = [[3, 4], [2], [1], [0, 4], [0, 3]]
V = [False] * len(G)
print(dfs(G, V, 0, 4))
print(dfs(G, V, 0, 1))
