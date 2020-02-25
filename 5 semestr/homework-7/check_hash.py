from collections import defaultdict

def checkhash(seq, f, mod):
    minc = None
    maxc = -1
    hash_dict = defaultdict(list)
    for el in seq:
        hash_dict[f(el) % mod].append(el)
    for el in hash_dict.values():
        if len(el) > maxc:
            maxc = len(el)
        if minc is None or (len(el) != 1 and len(el) < minc):
            minc = len(el)
    return (maxc, minc)
