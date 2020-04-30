def dislog(x, y, p):
    # pow(x,a,p)=yとなるaを求める(ない場合は-1を返す)
    m = int(p**0.5) + 1
    X = {pow(x, i, p): i for i in range(m)}
    r = pow(x, (p - 2) * m, p)
    t = y
    for i in range(m):
        try:
            return i * m + X[t]
        except BaseException:
            t = (t * r) % p
    return -1


x = 3
y = 193
p = 10**9 + 7
a = dislog(x, y, p)
print(a)
print(pow(x, a, p), y)
