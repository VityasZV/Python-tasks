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
        if sum_of_f_on_all_args(s, func) >= max_sum:
            max_f = func
    return max_f

print(maxfun([x/100000 for x in range(1,99999)], atan, atanh, ceil, cos, cosh, degrees, exp, fabs, floor, log10, log2, radians, sin, sinh, sqrt, tan, tanh))
