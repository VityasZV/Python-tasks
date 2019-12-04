from collections import defaultdict


class LetterAttr(object):
    def __init__(self):
        object.__setattr__(self, "_fields", defaultdict(set))

    def __getattr__(self, item):
        if item not in object.__getattribute__(self, "_fields").keys():
            object.__setattr__(self, item, item)
            object.__getattribute__(self, "_fields")[item] = set(item)
        return object.__getattribute__(self, item)

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        new_attr = ""
        if object.__getattribute__(self, "_fields")[key] == set():
            object.__getattribute__(self, "_fields")[key] = set(key)
            object.__setattr__(self, key, value)
        for i in value:
            if i in object.__getattribute__(self, "_fields")[key]:
                new_attr += i
        object.__setattr__(self, key, new_attr)
