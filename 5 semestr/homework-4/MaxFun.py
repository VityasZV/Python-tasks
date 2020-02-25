from math import *
def sum_of_f_on_all_args(args, f):
    summa = 0.0
    for elem in args:
        summa += f(elem)
    return summa

def maxfun(s, f1, *f):
    max_f = f1
    max_sum = sum_of_f_on_all_args(s, f1)
    for func in f:
        summa = sum_of_f_on_all_args(s, func)
        if summa >= max_sum:
            max_f = func
            max_sum = summa
    return max_f
