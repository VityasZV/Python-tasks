def sizer(class_arg):
    @property
    def size(self):
        pass

    @size.getter
    def size(self):
        if self._size is None:
            try:
                if getattr(class_arg, "__len__"):
                    return len(self)
            except AttributeError:
                return abs(int(self))
        else:
            return self._size

    @size.setter
    def size(self, value):
        self._size = value

    setattr(class_arg, "size", size)
    setattr(class_arg, "_size", None)
    return class_arg
