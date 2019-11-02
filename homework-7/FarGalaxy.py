from collections import defaultdict


def distance(a, b):
    return ((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)**0.5


def far_galaxy():
    galaxy = input().split(" ")
    result_g = 0
    result_d = 0
    all_galax = defaultdict(list)
    while len(galaxy) == 4:
        el = float(galaxy[0]), float(galaxy[1]), float(galaxy[2])
        all_galax[galaxy[3]].append(el)
        galaxy = input().split(" ")
    for gal in all_galax.keys():
        start = gal
        for points in all_galax[start]:
            for fin in all_galax.keys():
                for pointf in all_galax[fin]:
                    d = distance(points, pointf)
                    if d > result_d:
                        result_g = start, fin
                        result_d = d
    res = sorted(result_g)
    for el in res:
        print(el, end=" ")


far_galaxy()
