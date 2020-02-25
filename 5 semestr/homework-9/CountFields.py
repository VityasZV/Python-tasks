def count_methods_and_fields(class_arg):
    methods, fields = [], []
    for elem in dir(class_arg):
        if callable(getattr(class_arg, elem)) and elem[0:1] != "_":
            methods.append(elem)
        elif elem[0:1] != "_":
            fields.append(elem)
    return methods, fields


def fcounter(class_name, *args, **kwargs):
    class_object = class_name(*args, **kwargs)
    c_methods, c_fields = count_methods_and_fields(class_name)
    o_methods, o_fields = count_methods_and_fields(class_object)
    return (c_methods, c_fields, sorted(list(set(o_methods) - set(c_methods))),
            sorted(list(set(o_fields) - set(c_fields))))

