
# Допустим, вы ввели x, y, w, h, c
# x и y — это координаты некоторой клетки. Все клетки, лежащие между x и x+w по горизонтали, и y и y+h по вертикали(плюс идёт вниз), закрашиваются символом c
def TrimImage():
    s = input()
    x, y, w, h, c = s.split(" ")
    x, y, w, h = int(x), int(y), int(w), int(h)
    args = []
    while (x, y, w, h, c) != (0, 0, 0, 0, "0"):
        if (w != 0 and h != 0):
            args.append([x, y, w, h, c])
        s = input()
        x, y, w, h, c = s.split(" ")
        x, y, w, h = int(x), int(y), int(w), int(h)
    min_x = min(min(args[i][0] + args[i][2], args[i][0]) for i in range(len(args)))
    max_x = max(max(args[i][0] + args[i][2], args[i][0]) for i in range(len(args)))
    max_y = max(max(args[i][1] + args[i][3], args[i][1]) for i in range(len(args)))
    min_y = min(min(args[i][1] + args[i][3], args[i][1]) for i in range(len(args)))
    left_up_and_right_down = []
    for i in range(len(args)):
        x_left = min(args[i][0] + args[i][2], args[i][0]) - min_x
        y_left = min(args[i][1] + args[i][3], args[i][1]) - min_y
        x_right = max(args[i][0] + args[i][2], args[i][0]) - min_x
        y_right = max(args[i][1] + args[i][3], args[i][1]) - min_y
        c = args[i][4]
        new_el = [[x_left, y_left], [x_right, y_right], c]
        left_up_and_right_down.append(new_el)
    picture = []
    for j in range(abs(max_y - min_y)):
        line = []
        for i in range(abs(max_x - min_x)):
            line.append(".")
        picture.append(line)
    for new_el in left_up_and_right_down:
        c = new_el[2]
        for y in range(new_el[0][0], new_el[1][0], 1):
            for x in range(new_el[0][1], new_el[1][1], 1):
                picture[x][y] = new_el[2]
    for el in picture:
        for p in el:
            print(p, end='')
        print()


TrimImage()