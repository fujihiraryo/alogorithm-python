def circum_center(a, b, c):
    ax, ay = a
    bx, by = b
    cx, cy = c
    bc = ((bx - cx) ** 2 + (by - cy) ** 2) ** (1 / 2)
    ca = ((cx - ax) ** 2 + (cy - ay) ** 2) ** (1 / 2)
    ab = ((ax - bx) ** 2 + (ay - by) ** 2) ** (1 / 2)
    s = bc ** 2 * (ca ** 2 + ab ** 2 - bc ** 2)
    t = ca ** 2 * (ab ** 2 + bc ** 2 - ca ** 2)
    u = ab ** 2 * (bc ** 2 + ca ** 2 - ab ** 2)
    ox = (s * ax + t * bx + u * cx) / (s + t + u)
    oy = (s * ay + t * by + u * cy) / (s + t + u)
    return ox, oy
