def power(st):
    # 集合の冪集合を返す
    lst = list(st)
    l = len(st)
    powset = set()
    for i in range(2**l):
        subset = set()
        for j in range(l):
            if (i >> j) & 1 == 1:
                subset.add(lst[j])
        subset = frozenset(subset)
        powset.add(subset)
    return powset


# テスト
st = {1, 2, 3, 4}
print(power(st))