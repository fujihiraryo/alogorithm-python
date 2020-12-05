def edit_distance(s, t):
    m, n = len(s), len(t)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(m):
        for j in range(n):
            c = int(s[i] != t[j])
            dp[i + 1][j + 1] = min(dp[i][j + 1] + 1, dp[i + 1][j] + 1)
            dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + c)
    return dp[m][n]
