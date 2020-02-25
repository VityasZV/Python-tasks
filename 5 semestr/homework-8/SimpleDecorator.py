def nonify(func):
    def maybe_none(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == "" or result == False:
            return None
        else:
            return result
    return maybe_none
