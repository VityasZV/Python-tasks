def divider(m):
    _divider = "=" * m
    print(_divider)


def size(n):
    return len(str(n))


def mul_table(n, m):
    amount_of_columns = 1 + (m - 2 * size(n) - 7 - size(n**2)) // (2 * size(n) + 9 + size(n**2))
    for block_ind in range(n // amount_of_columns):
        divider(m)
        for str_ind in range(n):
            for k in range(amount_of_columns):
                first = f"{block_ind * amount_of_columns + k + 1}".rjust(size(n))
                second = f"{str_ind + 1}".ljust(size(n))
                third = f"{(block_ind * amount_of_columns + k + 1) * (str_ind + 1)}".ljust(size(n ** 2))
                print(first + " * " + second +
                      " = " + third, end='')
                if k != amount_of_columns - 1:
                    print(" | ", end='')
            print()
    divider(m)
    remained = n % amount_of_columns
    if remained != 0:
        for str_ind in range(n):
            for k in range(remained):
                print(f"{n - remained + k + 1}".rjust(size(n)) + " * " +
                      f"{str_ind + 1}".ljust(size(n)) + " = " +
                      f"{(n - remained + k + 1) * (str_ind + 1)}".ljust(size(n**2)), end='')
                if k != remained - 1:
                    print(" | ", end='')
            print()
        divider(m)


N, M = tuple(int(i) for i in input().split(","))
mul_table(N, M)
