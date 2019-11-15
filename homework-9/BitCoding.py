from collections import defaultdict
import operator
alphabet_10_64 = {i - 32: chr(i) for i in range(32, 96)}
alphabet_64_10 = {chr(i): i - 32 for i in range(32, 96)}

def shex(n):
    n_64 = ""
    while n > 0:
        n_64 += alphabet_10_64[n % 64]
        n //= 64
    return n_64[-1::-1]


def xehs(s):
    n = 0
    deg = 0
    for c in s[-1::-1]:
        n += alphabet_64_10[c]*(64**deg)
        deg += 1
    return n

def binary_to_64(s):
    n_10 = 0
    deg_10 = 0
    for c in s[-1::-1]:
        n_10 += (2**deg_10)*int(c)
        deg_10 += 1
    return shex(n_10)


def additional_sort(f):
    i = 0
    while i < len(f)-1:
        start = i
        finish = i
        for_sort = []
        while i < len(f)-1 and f[i][1] == f[i+1][1]:
            i += 1
            finish = i
        if start != finish:
            for_sort = f[start:finish+1]
            if len(for_sort):
                for_replace = sorted(for_sort, key=operator.itemgetter(0), reverse=True)
                for ind in range(start, finish+1):
                    f[ind] = for_replace[ind - start]
                i += 1
        else:
            i += 1
    result = "".join(el[0] for el in f)
    return result


def form_dict_for_coding(s):
    coding = defaultdict(str)
    amount_of_1 = 0
    for c in s:
        coding[c] = "1"*amount_of_1 + "0"
        amount_of_1 += 1
    return coding


def encode(txt):
    frequency = defaultdict(int)
    for c in txt:
        frequency[c] += 1
    s_frequency = sorted(frequency.items(), key=operator.itemgetter(1), reverse=True)
    string_sorted = additional_sort(s_frequency)
    coding_dict = form_dict_for_coding(string_sorted)
    encoded_string_demo = "".join(str(coding_dict[i]) for i in txt)
    encoded_string = binary_to_64(encoded_string_demo)
    return len(txt), string_sorted, encoded_string


# def decode(length, chars, code):


# print(alphabet_10_64)
# print(alphabet_64_10)

print(xehs("BREAKFAST"))
print(shex(10844745761445995))
res = encode("ENGINEERING WITHOUT MANAGEMENT IS ART.")
print(res)