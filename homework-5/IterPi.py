def pigen():
    n = 4.0
    i = 3
    is_minus = True
    yield n
    while True:
        if is_minus:
            n = n - 4/i
        else:
            n = n + 4/i
        yield n
        is_minus = not is_minus
        i += 2

