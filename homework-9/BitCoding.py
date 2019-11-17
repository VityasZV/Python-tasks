from collections import Counter
from math import ceil

def shex(n):
    bytes_l = []
    while n > 0:
        bytes_l.append(32 + (n & 63))
        n >>= 6
    return bytes(reversed(bytes_l)).decode("ASCII")

def xehs(s):
    n = 0
    for c in s:
        digit = ord(c) - 32
        n = n << 6 | digit
    return n


def encode(txt):
    s_frequency = list(sorted(list((j, i) for i, j in Counter(txt).most_common()), reverse=True))
    coding_dict = dict(list((s_frequency[i][1], "1" * i + "0") for i in range(len(s_frequency))))
    encoded_string_demo = "".join(coding_dict[i] for i in txt)
    encoded_string_demo += "0" * (ceil(len(encoded_string_demo) / 6) * 6 - len(encoded_string_demo))
    return len(txt), "".join(coding_dict.keys()), shex(int(encoded_string_demo, 2))


def decode(length, chars, code):
    coding_dict = dict(list(("1" * i + "0", chars[i]) for i in range(len(chars))))
    list_of_codes = (str(bin(xehs(code)))[2:] + "0").replace("0", "0 ").split()[:length]
    decoded_string = "".join(coding_dict[i] for i in list_of_codes)
    return decoded_string
