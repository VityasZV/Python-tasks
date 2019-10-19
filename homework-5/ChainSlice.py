from itertools import accumulate
from collections import deque
def chainslice(begin, end, *seq):
    sequence = deque()
    count = -1
    for el in seq:
        for i in el:
            count += 1
            if begin <= count < end:
                sequence.append(i)
            elif count >= end:
                break
        if count >= end:
            break
    return iter(sequence)


