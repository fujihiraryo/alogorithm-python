class Triangle():
    def __init__(self, A, B, C):
        # 3点の座標
        self.A = A
        self.B = B
        self.C = C
        Ax, Ay = A
        Bx, By = B
        Cx, Cy = C
        a = ((Bx - Cx)**2 + (By - Cy)**2)**0.5
        b = ((Cx - Ax)**2 + (Cy - Ay)**2)**0.5
        c = ((Ax - Bx)**2 + (Ay - By)**2)**0.5
        # 3辺の長さ
        self.a = a
        self.b = b
        self.c = c
        # 外心の座標
        s = a**2 * (b**2 + c**2 - a**2)
        t = b**2 * (c**2 + a**2 - b**2)
        u = c**2 * (a**2 + b**2 - c**2)
        Ux = (s * Ax + t * Bx + u * Cx) / (s + t + u)
        Uy = (s * Ay + t * By + u * Cy) / (s + t + u)
        self.U = (Ux, Uy)
        # 重心の座標
        self.G = ((Ax + Bx + Cx) / 3, (Ay + By + Cy) / 3)
        # 面積
        self.S = abs((Bx - Ax) * (Cy - Ay) - (Cx - Ax) * (By - Ay)) / 2
