def check_rect(point_or_line, prev_string, string):
    amount_of_rectangles = 0
    is_rect_started = 0
    for elem in zip(prev_string, string):
        if elem[0] == "#" and elem[1] == point_or_line:
            is_rect_started = 1
        elif is_rect_started:
            amount_of_rectangles += 1
            is_rect_started = 0
    return amount_of_rectangles


def find_rect():
    string = input()  # first -----
    string = input()
    amount_of_rectangles = 0
    previous_string = string # first real string
    string = input()
    while string[0] != "-":
        is_rect_started = 0
        amount_of_rectangles += check_rect(".", previous_string, string)
        previous_string = string
        string = input()
    is_rect_started = 0
    amount_of_rectangles += check_rect("-", previous_string, string)
    return amount_of_rectangles


print(find_rect())


