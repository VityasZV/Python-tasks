class WeAre:
    _count = 0
    def __init__(self):
        WeAre._count += 1

    def __del__(self):
        WeAre._count -= 1
        del self

    @property
    def count(self):
        return WeAre._count

    @count.getter
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        pass

    @count.deleter
    def count(self):
        pass

# a = WeAre()
# print(a.count)
# b, c = WeAre(), WeAre(),
# a.count = 100500
# print(a.count, b.count, c.count)
# del b.count
# del b
# print(a.count)