def distancePP(a, b):
    # 点aと点bの距離
    ax, ay = a
    bx, by = b
    return ((ax-bx)**2+(ay-by)**2)**0.5


def distanceLP(p, a, b):
    # 点pと直線abの距離
    px, py = p
    ax, ay = a
    bx, by = b
    return abs((ax-bx)*(ay-py)-(ax-px)*(ay-by))/distancePP(a, b)


def distanceSP(p, a, b):
    # 点pと線分abの距離
    px, py = p
    ax, ay = a
    bx, by = b
    if (ax-bx)*(ax-px)+(ay-by)*(ay-py) < 0:
        return distancePP(a, p)
    elif (bx-ax)*(bx-px)+(by-ay)*(by-py) < 0:
        return distancePP(b, p)
    else:
        return distanceLP(p, a, b)


# テスト
a, b = (1, 1), (2, 3)
print(distancePP(a, b))
p = (1, 0)
print(distanceLP(p, a, b))
print(distanceSP(p, a, b))
