def statcounter():
    function_using = {}
    function_using_new = yield function_using

    def counter(func):
        function_using.setdefault(func, 0)

        def wrapper(*args, **kwargs):
            function_using[func] += 1
            res = func(*args, **kwargs)
            return res

        return wrapper

    while function_using_new:
        function_using_new = yield counter(function_using_new)
