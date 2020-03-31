def all_sub(lst):
    # リストの部分リストを全列挙する
    n = len(lst)
    lstlst = []
    for i in range(2**n):
        sublst = []
        for j in range(n):
            if (i >> j) & 1 == 1:
                sublst.append(lst[j])
        lstlst.append(sublst)
    return lstlst


# テスト
lst = list(range(10))
print(all_sub(lst))
