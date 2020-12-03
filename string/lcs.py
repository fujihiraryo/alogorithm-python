def lcs(S, T):
    # 最長共通部分列
    m, n = len(S), len(T)
    C = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if S[i] == T[j]:
                C[i + 1][j + 1] = C[i][j] + 1
            else:
                C[i + 1][j + 1] = max(C[i][j + 1], C[i + 1][j])
    le = C[m][n]
    X = ""
    while le:
        if S[m - 1] == T[n - 1]:
            X = S[m - 1] + X
            m -= 1
            n -= 1
            le -= 1
        elif C[m][n] == C[m - 1][n]:
            m -= 1
        else:
            n -= 1
    return X


S = "abracadabra"
T = "avadakedavra"
print(lcs(S, T))
