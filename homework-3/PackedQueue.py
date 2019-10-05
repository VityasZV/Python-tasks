def transform_tuples_into_list_and_separate_ints(arguments):
    list_of_tuples = []
    list_of_ints = []

    for arg in arguments:
        if type(arg) == tuple:
            for elem in arg:
                list_of_tuples.append(elem)
        else:
            list_of_ints.append(arg)
    return list_of_tuples, list_of_ints


def form_tuple(elements_from_tuples, needed_amount):
    if needed_amount == 0:
        print(tuple())
        return
    else:
        tuple_for_print = tuple(elements_from_tuples[i] for i in range(needed_amount))
        print(tuple_for_print)
        for i in range(needed_amount):
            elements_from_tuples.pop(0)
        return


def packed_queue():
    arguments = eval(input())
    all_tuples_elements, all_ints = transform_tuples_into_list_and_separate_ints(arguments)
    for integer in all_ints:
        if len(all_tuples_elements) <= integer:
            break
        else:
            form_tuple(all_tuples_elements, integer)


packed_queue()
