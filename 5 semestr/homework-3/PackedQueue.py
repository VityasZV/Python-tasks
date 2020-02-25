from collections import deque


def form_tuple(elements_from_tuples, needed_amount):
    if needed_amount == 0:
        print(tuple())
        return
    else:
        tuple_for_print = tuple(elements_from_tuples[i] for i in range(needed_amount))
        print(tuple_for_print)
        for i in range(needed_amount):
            elements_from_tuples.popleft()
        return


def packed_queue():
    arguments = eval(input())
    deq_of_tuple_elements = deque()
    for arg in arguments:
        if type(arg) == tuple:
            for elem in arg:
                deq_of_tuple_elements.append(elem)
        elif type(arg) == int:
            if len(deq_of_tuple_elements) < arg:
                break
            else:
                form_tuple(deq_of_tuple_elements, arg)


packed_queue()
