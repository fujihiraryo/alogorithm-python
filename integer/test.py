n = 262144


def is_prime(x):
    for i in range(2, int(x**0.5+2)):
        if x % i == 0:
            return False
    return True


for a in range(10000, 20000):
    for w in range(2, 100):
        p = a*n+1
        if is_prime(p) and pow(w, n, p) == 1:
            print(p, w)
