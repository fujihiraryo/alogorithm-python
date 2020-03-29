def trisect(f, eps=10**(-5)):
    # 凸関数fのargminとminの近似値を求める
    left = 0.1
    right = 2
    while right - left > 0.0001:
        left_ = left + (right - left) * (1 / 3)
        right_ = left + (right - left) * (2 / 3)
        if f(left_) <= f(right_):
            right = right_
        else:
            left = left_
    x = (left + right) / 2
    return x, f(x)


# テスト
def f(x):
    return x + 1 / x


print(trisect(f))
