def count_methods_and_fields(class_arg):
    methods, fields = [], []
    for elem in dir(class_arg):
        if callable(getattr(class_arg, elem)) and elem[0:2] != "__":
            methods.append(elem)
        elif elem[0:2] != "__":
            fields.append(elem)
    return methods, fields


def fcounter(class_name, *args):
    class_object = class_name(*args)
    c_methods, c_fields = count_methods_and_fields(class_name)
    o_methods, o_fields = count_methods_and_fields(class_object)
    return c_methods, c_fields, o_methods, o_fields