def ternary_search(f, left, right, absolute_precision):
    while right - left > absolute_precision:
        left_third = left + (right - left) / 3
        right_third = right - (right - left) / 3
        if f(left_third) <= f(right_third):
            right = right_third
        else:
            left = left_third
    return (left + right) / 2
