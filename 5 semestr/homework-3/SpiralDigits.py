def increment():
    i = 0
    yield i
    while True:
        i += 1
        if i == 10:
            i = 0
        yield i


def spiral_digits():
    columns, strings = tuple(int(x) for x in input().split(","))
    matrix = []
    # initialization by seroes
    for s in range(strings):
        matrix.append([])
        matrix[s] = [0 for i in range(columns)]

    generator = increment()
    i = next(generator)  # using for [0..9]

    up = 0  # using for up start
    down = strings-1  # using for down border
    left = 0  # using for going from left to right
    right = columns-1  # using as right border
    while up != down and left != right:
        old_left, old_right, old_up, old_down = left, right, up, down
        while left <= right:
            matrix[up][left] = i
            left += 1
            i = next(generator)
        left = old_left
        up += 1
        while up <= down:
            matrix[up][right] = i
            up += 1
            i = next(generator)
        up = old_up
        right -= 1
        while right >= left:
            matrix[down][right] = i
            right -= 1
            i = next(generator)
        right = old_right
        down -= 1
        while down > up:
            matrix[down][left] = i
            down -= 1
            i = next(generator)
        down = old_down
        up, left, right, down = up + 1, left + 1, right - 1, down - 1
        if up == down or left == right:
            break
        if up > down or left > right:
            break
    if up == down and left == right:
        matrix[up][left] = i
    else:
        if up == down:
            while left <= right:
                matrix[up][left] = i
                left += 1
                i = next(generator)
        elif left == right:
            while up <= down:
                matrix[up][left] = i
                up += 1
                i = next(generator)
    for i in range(strings):
        for j in range(columns):
            print(matrix[i][j], end=' ')
        print()


if __name__ == "__main__":
    spiral_digits()
