def bisect(f, left, right):
    # はじめてf(x)=Trueになるxを求める
    if right-left == 1:
        return right
    mid = (left+right)//2
    if f(mid):
        right = mid
        return bisect(f, left, right)
    else:
        left = mid
        return bisect(f, left, right)


def f(x):
    return 2**x > 10000


print(bisect(f, -100, 1000))
