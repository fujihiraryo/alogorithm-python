def ext_euclid(a, b):
    # 互いに素なa,bに対して、方程式ax+by=1の整数解を1つ求める
    x0, y0, r0 = 1, 0, a
    x1, y1, r1 = 0, 1, b
    while r0:
        x0, x1 = x1 - x0 * (r1 // r0), x0
        y0, y1 = y1 - y0 * (r1 // r0), y0
        r0, r1 = r1 % r0, r0
    return x1, y1, r1


def mod_inv(a, m):
    x, _, r = ext_euclid(a, m)
    if r != 1:
        return -1
    return x % m
