def top_sort(G, L):
    n = len(G)
    S = [i for i in range(n) if L[i] == 0]
    A = []
    while S:
        i = S.pop()
        A.append(i)
        while G[i]:
            j = G[i].pop()
            L[j] -= 1
            if L[j] == 0:
                S.append(j)
    return A


G = [[3, 6, 7], [3, 4], [0], [], [7], [0, 4], [], []]
L = [2, 0, 0, 2, 2, 0, 1, 2]
print(top_sort(G, L))
