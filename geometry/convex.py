def counter_clock(a, b, p):
    # 線分abに対してpが反時計回りにあるか
    ax, ay = a
    bx, by = b
    px, py = p
    return (bx-ax)*(py-ay) > (by-ay)*(px-ax)


def convex(P):
    # 点群Pの凸包
    P.sort()
    n = len(P)
    U = []
    for i in range(n):
        if i < 2:
            U.append(P[i])
            continue
        a, b, p = U[-2], U[-1], P[i]
        while counter_clock(a, b, p) and len(U) > 2:
            U.pop()
            a, b = U[-2], U[-1]
        U.append(p)
    L = []
    for i in range(n):
        if i < 2:
            L.append(P[i])
            continue
        a, b, p = L[-2], L[-1], P[i]
        while not counter_clock(a, b, p) and len(L) > 2:
            L.pop()
            a, b = L[-2], L[-1]
        L.append(p)
    return list(set(U+L))


# テスト
P = [(0, 0), (1, 2), (2, 1), (5, 0), (2, -1), (1, -2)]
print(convex(P))
