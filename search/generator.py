def generator(n, r):
    # n個からr個を重複を許して取り出す組合せ
    if r == 0:
        yield []
    else:
        a = 0
        for A in generator(n, r - 1):
            if r > 1:
                a = A[-1]
            for i in range(a, n):
                A.append(i)
                yield A
                A.pop()


for A in generator(6, 3):
    print(A)
