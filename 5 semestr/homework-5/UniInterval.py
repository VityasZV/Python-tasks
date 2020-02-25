def UniInterval():
    intervals = eval(input())
    left_points = list((el[0], False) for el in intervals)
    right_points = list((el[1], True) for el in intervals)
    all_points = sorted(left_points + right_points)
    result = 0
    flag = 0
    for i in range(len(all_points)):
        if flag:
            result += all_points[i][0] - all_points[i - 1][0]
        if all_points[i][1]:
            flag += 1
        else:
            flag -= 1
    print(result)


UniInterval()