def bellman_ford(G, r):
    # rを始点とする各点へのパスの長さを求める
    n = len(G)
    E = []
    for i in range(n):
        for j in G[i].keys():
            E.append((i, j, G[i][j]))
    inf = 10**20
    D = [inf for i in range(n)]
    D[r] = 0
    flag = True
    cnt = 0
    while flag:
        flag = False
        cnt += 1
        if cnt > n:
            return
        for s, t, d in E:
            if D[s] != inf and D[t] > D[s] + d:
                D[t] = D[s] + d
                flag = True
    return D
