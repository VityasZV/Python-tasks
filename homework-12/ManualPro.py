from collections import Counter
def is_only_object_remains(mros):
    for el in mros:
        if el != ["object"]:
            return False
    else:
        return True

def merge(mros_of_classes):
    result = []
    while not is_only_object_remains(mros_of_classes):
        ischanged = False
        for i in range(len(mros_of_classes)):
            pos = mros_of_classes[i][0]
            isgood = True

            for j in range(len(mros_of_classes)):
                if j == i: continue
                if pos in mros_of_classes[j] and mros_of_classes[j][0] != pos:
                    isgood = False
                    break
            if isgood:
                ischanged = True
                result.append(pos)
                for j in range(len(mros_of_classes)):
                    if mros_of_classes[j][0] == pos:
                        mros_of_classes[j].pop(0)
                break
        if not ischanged:
            return -1
    result.append('object')
    return result

def ccheck(*classes):
    try:
        l = []
        for i in classes:
            el = []
            for j in i.mro():
                el.append(j.__name__)
            l.append(el)
        result = merge(l)
        needed_classes = []
        for i in result:
            for j in classes:
                if j.__name__ == i:
                    needed_classes.append(j)
        class Checked(*tuple(needed_classes)):
            pass
        return Checked
    except BaseException as ERR:
        class Checked(object):
            pass

        return Checked


class A: pass


class B(A): pass


class C(A): pass


class D(B, C): pass


class E(C, B): pass


print(*(c.__name__ for c in ccheck(A, B).mro()))
print(*(c.__name__ for c in ccheck(D, E).mro()))
