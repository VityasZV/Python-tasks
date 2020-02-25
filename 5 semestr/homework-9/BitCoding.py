from collections import Counter, deque
from math import ceil

alf = {i: chr(i + 32) for i in range(64)}
alf_rev = {chr(i + 32): i for i in range(64)}

def shex(n):
    bytes_l = deque()
    demo_k = bin(n)[2:]
    needed_zeroes = 1 if len(demo_k) % 6 != 0 else 0
    k = (6 - len(demo_k) % 6)*needed_zeroes * "0" + demo_k
    for i in range(0, len(k), 6):
        bytes_l.append(alf[int(k[i:i+6], 2)])
    return "".join(c for c in bytes_l)



def xehs(s):
    n = deque()
    for c in s:
        digit = bin(alf_rev[c])[2:]
        n.append(digit.rjust(6, "0"))
    return int(str().join(i for i in n), 2)


def encode(txt):
    s_frequency = sorted(list((j, i) for i, j in Counter(txt).most_common()), reverse=True)
    coding_dict = dict((s_frequency[i][1], "1" * i + "0") for i in range(len(s_frequency)))
    encoded_string_demo = "".join(coding_dict[i] for i in txt)
    demo_len = len(encoded_string_demo)
    encoded_string_demo += "0" * (ceil(demo_len / 6) * 6 - demo_len)
    return len(txt), "".join(coding_dict.keys()), shex(int(encoded_string_demo, 2))


def decode(length, chars, code):
    coding_dict = dict(("1" * i + "0", chars[i]) for i in range(len(chars)))
    list_of_codes = (bin(xehs(code))[2:]).replace("0", "0 ").split()[:length]
    decoded_string = "".join(coding_dict[i] for i in list_of_codes)
    return decoded_string
