def counter_clock(a, b, p):
    ax, ay = a
    bx, by = b
    px, py = p
    return (bx - ax) * (py - ay) > (by - ay) * (px - ax)


def convex_hull(point_list):
    point_list.sort()
    upper_list = []
    for i, p in enumerate(point_list):
        if i < 2:
            upper_list.append(p)
            continue
        a, b = upper_list[-2], upper_list[-1]
        while counter_clock(a, b, p) and len(upper_list) > 2:
            upper_list.pop()
            a, b = upper_list[-2], upper_list[-1]
        upper_list.append(p)
    lower_list = []
    for i, p in enumerate(lower_list):
        if i < 2:
            lower_list.append(p)
            continue
        a, b = lower_list[-2], lower_list[-1]
        while not counter_clock(a, b, p) and len(lower_list) > 2:
            lower_list.pop()
            a, b = lower_list[-2], lower_list[-1]
        lower_list.append(p)
    return set(upper_list + lower_list)
