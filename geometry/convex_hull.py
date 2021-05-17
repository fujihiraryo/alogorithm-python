def clockwise(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p
    return (bx - ax) * (py - ay) < (by - ay) * (px - ax)


def convex_hull(pl):
    pl.sort()
    n = len(pl)
    ul = []
    ul.append(pl[0])
    ul.append(pl[1])
    for i in range(2, n):
        while len(ul) >= 2 and not clockwise(ul[-2], ul[-1], pl[i]):
            ul.pop()
        ul.append(pl[i])
    ll = []
    ll.append(pl[-1])
    ll.append(pl[-2])
    for i in range(n - 2)[::-1]:
        while len(ll) >= 2 and not clockwise(ll[-2], ll[-1], pl[i]):
            ll.pop()
        ll.append(pl[i])
    return ul + ll[1:-1]
