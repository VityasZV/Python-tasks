from collections import defaultdict
from collections import deque

def distance(a, b):
    return (b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2 #without sqrt


def far_galaxy():
    galaxy = input().split(" ")
    result_g = galaxy[3]
    result_d = 0
    all_galax = defaultdict(deque)
    while len(galaxy) == 4:
        el = float(galaxy[0]), float(galaxy[1]), float(galaxy[2])
        all_galax[galaxy[3]].append(el)
        galaxy = input().split(" ")
    if len(all_galax.keys()) == 1:
        print(result_g, " ", result_g)
        return
    remained = set(all_galax.keys())
    for start in all_galax.keys():
        remained = remained.difference({start})
        for points in all_galax[start]:
            for fin in remained:
                for pointf in all_galax[fin]:
                    d = distance(points, pointf)
                    if d > result_d:
                        result_g = start, fin
                        result_d = d
    res = sorted(result_g)
    for el in res:
        print(el, end=" ")


far_galaxy()
