def divider(m):
    _divider = "=" * m
    print(_divider)

def start_wide_count(n):
    n = n * n
    res = 0
    while n > 0:
        n = n // 10
        res += 1
    return res


def wide_count(n):
    res = 0
    while n > 0:
        n = n // 10
        res += 1
    return res

def set_spaces(k, w):
    s = " " * (w - k)
    return s

def mul_table(n, m):
    divider(m)
    wide = start_wide_count(n)
    w_sum = 0
    i_right = n + 1
    i_left = 1
    wide_str = 0
    wide_str_fin = 0
    for j in range(1, n + 1):
        for i in range(i_left, i_right):
            ends = " | " if i < i_right-1 else f"\n"
            s = f" {i} * {j}{set_spaces(wide_count(j), wide-1)} = {i*j}{set_spaces(wide_count(i*j), wide)}{ends}"
            w_sum += len(s)
            if w_sum <= m:
                print(s, end='')
                if m - w_sum <= 3:
                    w_sum = 0
            else:
                if i != n:
                    w_sum -= 3
                    if w_sum <= m:
                        s = s[:-3]
                        print(s, end='')

                wide_str_fin = w_sum
                w_sum = 0
                i_right = i + 1
                print()
                break
    divider(m)


N, M = tuple(int(i) for i in input().split(","))
mul_table(N, M)
