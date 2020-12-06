def distance_pp(a, b):
    ax, ay = a
    bx, by = b
    return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5


def distance_lp(p, a, b):
    # 点pと直線abの距離
    px, py = p
    ax, ay = a
    bx, by = b
    c = (ax - bx) * (ay - py) - (ax - px) * (ay - by)
    return abs(c / distance_pp(a, b))


def distance_sp(p, a, b):
    # 点pと線分abの距離
    px, py = p
    ax, ay = a
    bx, by = b
    if (ax - bx) * (ax - px) + (ay - by) * (ay - py) < 0:
        return distance_pp(a, p)
    elif (bx - ax) * (bx - px) + (by - ay) * (by - py) < 0:
        return distance_pp(b, p)
    else:
        return distance_lp(p, a, b)
