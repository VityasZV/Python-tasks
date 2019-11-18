from collections import Counter, deque
from math import ceil

def shex(n):
    bytes_l = deque()
    while n > 0:
        bytes_l.appendleft(chr(32 + (n & 63)))
        n >>= 6
    return "".join(c for c in bytes_l)


def xehs(s):
    n = 0
    for c in s:
        digit = ord(c) - 32
        n = n << 6 | digit
    return n


def encode(txt):
    s_frequency = sorted(list((j, i) for i, j in Counter(txt).most_common()), reverse=True)
    coding_dict = dict((s_frequency[i][1], "1" * i + "0") for i in range(len(s_frequency)))
    encoded_string_demo = "".join(coding_dict[i] for i in txt)
    demo_len = len(encoded_string_demo)
    encoded_string_demo += "0" * (ceil(demo_len / 6) * 6 - demo_len)
    return len(txt), "".join(coding_dict.keys()), shex(int(encoded_string_demo, 2))


def decode(length, chars, code):
    coding_dict = dict(("1" * i + "0", chars[i]) for i in range(len(chars)))
    list_of_codes = (bin(xehs(code))[2:] + "0").replace("0", "0 ").split()[:length]
    decoded_string = "".join(coding_dict[i] for i in list_of_codes)
    return decoded_string
