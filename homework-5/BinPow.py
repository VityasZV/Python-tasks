def BinPow(a, n, f):
    if n == 1:
        return a
    elif n == 2:
        return f(a, a)
    else:
        return f(BinPow(a, n // 2, f), BinPow(a, n // 2 if n % 2 == 0 else n//2 + 1, f))

