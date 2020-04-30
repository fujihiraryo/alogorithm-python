def warshall_floyd(G):
    inf = 10**18
    # 重みつきグラフGに対してすべての頂点対の距離を求める
    n = len(G)
    D = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        D[i][i] = 0
        for j in G[i].keys():
            D[i][j] = G[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


# テスト
G = [{1: 5, 2: 1}, {0: 5, 2: 1}, {0: 1, 1: 1}, {}]
print(warshall_floyd(G))
