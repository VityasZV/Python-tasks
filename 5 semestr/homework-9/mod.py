old_a, old_b, old_d, old_fiction = None, None, None, None
working_a = old_a
count = 0


def check(a, b, d, f):
    if (globals()["old_a"], globals()["old_b"], globals()["old_d"], globals()["old_fiction"]) == (a, b, d, f):
        return True
    else:
        return False


def randrange(a, b=None, d=1, fiction=None):
    if check(a, b, d, fiction):
        globals()["working_a"] += d
        if b is None:
            if globals()["working_a"] < a:
                return globals()["working_a"]
            else:
                globals()["working_a"] = 0
                return globals()["working_a"]
        else:
            if b > a:
                if globals()["working_a"] < b:
                    return globals()["working_a"]
                else:
                    globals()["working_a"] = a + globals()["working_a"] % b
                    return globals()["working_a"]
            else:
                if globals()["working_a"] > b:
                    return globals()["working_a"]
                else:
                    globals()["working_a"] = a - (a + globals()["working_a"]) % b if globals()["working_a"] != b else a
                    return globals()["working_a"]
    else:
        globals()["old_a"], globals()["old_b"], globals()["old_d"], globals()["old_fiction"] = a, b, d, fiction
        if b is None:
            globals()["working_a"] = 0
        else:
            globals()["working_a"] = a
        return globals()["working_a"]


def randint(a, b):
    result = b if globals()["count"] % 2 else a
    globals()["count"] += 1
    return result
