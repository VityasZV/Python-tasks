from math import *


def fix(n):
    def try_rounding(func):
        def rounding(*args, **kwargs):
            r_args = tuple(round(i, n) if type(i) == float else i for i in args)
            r_kargs = dict.fromkeys(kwargs.keys())
            for k in kwargs.keys():
                r_kargs[k] = round(kwargs[k], n) if type(kwargs[k]) == float else kwargs[k]
            result = func(*r_args, **r_kargs)
            if type(result) == float:
                return round(result, n)
            else:
                return result

        return rounding

    return try_rounding

