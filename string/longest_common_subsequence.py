def longest_common_subsequence(s, t):
    m, n = len(s), len(t)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if s[i] == t[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    tmp = dp[m][n]
    res = ""
    while tmp:
        if s[m - 1] == t[n - 1]:
            res = s[m - 1] + res
            m -= 1
            n -= 1
            tmp -= 1
        elif dp[m][n] == dp[m - 1][n]:
            m -= 1
        else:
            n -= 1
    return res


if __name__ == "__main__":
    s = "abracadabra"
    t = "avadakedavra"
    print(longest_common_subsequence(s, t))
