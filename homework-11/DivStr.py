import inspect


class DivStr(str):
    def __init__(self, arg):
        self.val = str(arg)

    def __truediv__(self, other):
        if other > len(self.val):
            return DivStr("")
        return DivStr(self.val[:len(self.val) // other])

    for i in str.__dict__:
        attr = getattr(str, i)
        if callable(attr):
            if i not in ["__class__", "__new__", "__getattribute__", "__getattr__", "__repr__", "__str__"]:
                if inspect.getmembers(eval(f"str.{i}"))[-1] == ('__text_signature__', '($self, /)'):
                    exec(f"def {i}(self): return DivStr(self.val.{i}())")
                else:
                    exec(f"def {i}(self, *args, **kwargs): return DivStr(self.val.{i}(*args, **kwargs))")

    def __len__(self):
        return len(self.val)

