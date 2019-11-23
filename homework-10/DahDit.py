from collections import deque


class morse:
    alphabet = {"+": "di", "-": "dah", "~": ","}
    ending = "."
    plus_in_the_end = "dit"
    alphabet_end = {"+": "dit", "-": "dah"}
    separator = " "

    def __init__(self, str_argument=""):
        self.buffer = deque()
        str_argument = str_argument.split(" ")
        if len(str_argument) == 1:
            if len(str_argument[0]) == 2:
                self.alphabet["~"] = " "
                self.separator = ""
                self.alphabet["-"] = str_argument[0][1]
                self.alphabet["+"] = str_argument[0][0]
                self.alphabet_end['+'] = self.alphabet["+"]
                self.alphabet_end["-"] = self.alphabet["-"]
                self.ending = ""
            elif len(str_argument[0]) == 3:
                self.separator = ""
                self.alphabet["+"] = str_argument[0][0]
                self.alphabet_end["+"] = str_argument[0][1]
                self.alphabet["-"] = str_argument[0][2]
                self.alphabet_end["-"] = self.alphabet["-"]
                self.alphabet["~"] = " "
                self.ending = ""
            elif len(str_argument[0]) == 4:
                self.separator = ""
                self.alphabet["+"] = str_argument[0][0]
                self.alphabet_end["+"] = str_argument[0][1]
                self.alphabet["-"] = str_argument[0][2]
                self.alphabet_end["-"] = self.alphabet["-"]
                self.alphabet["~"] = " "
                self.ending = str_argument[0][3]
        elif len(str_argument) == 2:
            self.alphabet["~"] = " "
            self.separator = ""
            self.alphabet["-"] = str_argument[1]
            self.alphabet["+"] = str_argument[0]
            self.alphabet_end = self.alphabet
        elif len(str_argument) == 3:
            self.alphabet["+"] = str_argument[0]
            self.alphabet_end["+"] = str_argument[1]
            self.alphabet["-"] = str_argument[2]
            self.alphabet_end["-"] = self.alphabet["-"]
            self.alphabet["~"] = ","
        elif len(str_argument) == 4:
            self.alphabet["+"] = str_argument[0]
            self.alphabet_end["+"] = str_argument[1]
            self.alphabet["-"] = str_argument[2]
            self.alphabet_end["-"] = self.alphabet["-"]
            self.alphabet["~"] = ","
            self.ending = str_argument[3]

    def __str__(self):
        res = ""
        if len(self.buffer) == 0:
            return self.ending
        for i in range(len(self.buffer)):
            el, next_el = self.buffer[i], self.buffer[i + 1] if i < len(self.buffer) - 1 else None
            sep = self.separator if next_el != "~" and next_el is not None else ""
            res += self.check(el, next_el) + sep
        return res.lstrip()

    def __pos__(self):
        self.buffer.appendleft("+")
        return self

    def __neg__(self):
        self.buffer.appendleft("-")
        return self

    def __invert__(self):
        self.buffer.appendleft("~")
        return self

    def check(self, element, next_element=None):
        if not next_element:
            return self.alphabet_end[element] + self.ending
        else:
            if element == "~":
                return self.alphabet[element]
            if next_element == "~":
                return self.alphabet_end[element]
            else:
                return self.alphabet[element]

print(--+~-~-++~+++-morse("ai aui oi "))