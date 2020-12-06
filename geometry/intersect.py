def intersect(a, b, c, d):
    # 線分abとcdの交差判定(端点含む)
    ax, ay = a
    bx, by = b
    cx, cy = c
    dx, dy = d
    ta = (cx - dx) * (ay - cy) + (cy - dy) * (cx - ax)
    tb = (cx - dx) * (by - cy) + (cy - dy) * (cx - bx)
    tc = (ax - bx) * (cy - ay) + (ay - by) * (ax - cx)
    td = (ax - bx) * (dy - ay) + (ay - by) * (ax - dx)
    return tc * td <= 0 and ta * tb <= 0
