MOD = 10 ** 9 + 7
n = 10 ** 6

inv = [None] * (n + 1)
inv[1] = 1
for i in range(2, n + 1):
    inv[i] = -(MOD // i) * inv[MOD % i] % MOD

fct = [1] * (n + 1)
ifc = [1] * (n + 1)
for i in range(1, n + 1):
    fct[i] = fct[i - 1] * i % MOD
    ifc[i] = ifc[i - 1] * inv[i] % MOD


def cmb(x, y):
    if x < y or x < 0 or y < 0:
        return 0
    else:
        return fct[x] * ifc[x - y] * ifc[y] % MOD
