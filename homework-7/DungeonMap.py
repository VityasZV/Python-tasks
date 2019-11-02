from collections import defaultdict


def tunnels_from_input():
    tunnels = defaultdict(set)
    a_to_b = input().split(" ")
    a = tuple()
    while len(a_to_b) != 1:
        tunnels[a_to_b[0]].add(a_to_b[1])
        tunnels[a_to_b[1]].add(a_to_b[0])
        a_to_b = input().split(" ")
    beg = a_to_b[0]
    en = input()
    return [beg, en, tunnels]


def check(dungeons, en):
    #print(s)
    res = True if en in dungeons else False
    return res


def way_check(tunnels, pos_way_l, dungeons, ending):
    new_dungeons = set(tunnels[pos_way_l[-1]])
    #print(new_dungeons)
    if check(new_dungeons, ending):
        return True
    else:
        for el in new_dungeons.difference(dungeons):
            pos_way_l.append(el)
            if way_check(tunnels, pos_way_l, dungeons.union({el}), ending):
                return True
            pos_way_l.pop()
        return False


def is_way_exist(beg_end_tunnels):
    begin = beg_end_tunnels[0]
    ending = beg_end_tunnels[1]
    tunnels = beg_end_tunnels[2]
    #print(tunnels, begin, ending)
    if tunnels[begin] == set() or tunnels[ending] == set():
        return "NO"
    p = list()
    p.append(begin)
    d = set()
    d.add(begin)
    res = way_check(tunnels, p, d, ending)
    answer = "YES" if res else "NO"
    return answer


print(is_way_exist(tunnels_from_input()))
