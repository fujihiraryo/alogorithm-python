class Circle():
    # 中心p、半径rの円
    def __init__(self, p, r):
        self.p = p
        self.r = r

    def contain(self, q):
        # 点qを含むか判定
        px, py = self.p
        qx, qy = q
        return (px-qx)**2+(py-qy)**2 <= self.r**2
