def binary_search(f, left, right):
    while right - left > 1:
        mid = (left + right) // 2
        if f(mid):
            right = mid
        else:
            left = mid
    return right
