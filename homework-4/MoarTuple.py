def count_dividends_from_tuple_on_n(tup, n):
    count = 0
    for elem in tup:
        if elem % n == 0:
            count+=1
    return count


def moar(a, b, n):
    return count_dividends_from_tuple_on_n(a, n) > \
           count_dividends_from_tuple_on_n(b, n)

