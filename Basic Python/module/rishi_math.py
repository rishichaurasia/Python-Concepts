def factorial_rec(x):
    if x == 0:
        return 1
    else:
        return x * factorial_rec(x - 1)


def factorial(x):
    if x == 0:
        return 1
    fac = 1
    for i in range(x, 0, -1):
        fac *= i
    return fac
