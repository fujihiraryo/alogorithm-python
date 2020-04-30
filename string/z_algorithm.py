def zalgo(S):
    # SとS[i:n]の最長共通接頭辞の長さを記録した配列を返す
    n = len(S)
    A = [0] * n
    j = 0
    for i in range(1, n):
        if i + A[i - j] < j + A[j]:
            A[i] = A[i - j]
        else:
            k = max(0, A[j] - i + j)
            while i + k < n and S[k] == S[i + k]:
                k += 1
            A[i] = k
            j = i
    A[0] = n
    return A


S = 'aaabaaaab'
print(zalgo(S))
