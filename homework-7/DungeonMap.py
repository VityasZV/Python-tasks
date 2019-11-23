from collections import defaultdict


def tunnels_from_input():
    tunnels = defaultdict(set)
    a_to_b = input().split(" ")
    while len(a_to_b) != 1:
        tunnels[a_to_b[0]].add(a_to_b[1])
        tunnels[a_to_b[1]].add(a_to_b[0])
        a_to_b = input().split(" ")
    beg = a_to_b[0]
    en = input()
    return [beg, en, tunnels]


def check(dungeons, en):
    res = True if en in dungeons else False
    return res


def way_check(tunnels, begin, ending):  # dungeons is just begin
    all_dungeons = set(tunnels.keys())
    new_dungeons = tunnels[begin]
    old_dungeons = {begin}
    if check(new_dungeons.union(old_dungeons), ending):
        return True
    else:
        un = old_dungeons.union(new_dungeons)
        while un != old_dungeons:
            old_dungeons = un
            save = new_dungeons
            l = list()
            for el in save:
                app = list(i for i in tunnels[el])
                l = l + app
            new_dungeons = set(l).difference(old_dungeons)
            if check(new_dungeons, ending):
                return True
            un = old_dungeons.union(new_dungeons)
        return False


def is_way_exist(beg_end_tunnels):
    begin = beg_end_tunnels[0]
    ending = beg_end_tunnels[1]
    tunnels = beg_end_tunnels[2]
    if tunnels[begin] == set() or tunnels[ending] == set():
        return "NO"
    res = way_check(tunnels, begin, ending)
    answer = "YES" if res else "NO"
    return answer


print(is_way_exist(tunnels_from_input()))
