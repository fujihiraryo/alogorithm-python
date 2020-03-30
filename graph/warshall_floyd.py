def warshall_floyd(G):
    inf = 10**18
    # 重みつきグラフGに対してすべての頂点対の距離を求める
    n = len(G)
    d = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        d[i][i] = 0
        for j in G[i].keys():
            d[i][j] = G[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d


# テスト
G = [{1: 5, 2: 1}, {0: 5, 2: 1}, {0: 1, 1: 1}, {}]
print(warshall_floyd(G))
