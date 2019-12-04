class DivStr(str):
    def __init__(self, arg):
        self.val = str(arg)

    def __truediv__(self, other):
        if other > len(self.val):
            return DivStr("")
        return DivStr(self.val[:len(self.val) // other])

    for method_name, method in str.__dict__.items():
        if callable(method) and method_name not in ["__class__", "__new__", "__getattribute__",
                                                    "__getattr__", "__repr__", "__str__"]:
            exec(f"def {method_name}(self, *args, **kwargs):\n"
                 f" str_result = str.{method_name}(self, *args)\n"
                 f" if isinstance(str_result, str):\n"
                 f"     return DivStr(str_result)\n"
                 f" else:\n"
                 f"     return str_result")
