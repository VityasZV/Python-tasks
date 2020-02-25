from fractions import Fraction
from math import ceil, floor
import copy

class sausage:
    horizontal_size = 12

    def __init__(self, farsh=None, size=""):
        self.size = Fraction(size) if size else Fraction("1")
        self.farsh = farsh if farsh else "pork!"
   
    def __str__(self):
        if self.size <= 0:
            return "/|\n||\n||\n||\n\|"
        amount_of_pieces = floor(self.size)
        remains = self.size - amount_of_pieces
        remains = self.horizontal_size * remains.numerator / remains.denominator
        if floor(remains) != remains:
            return "/|\n||\n||\n||\n\|"
        remains = floor(remains)
        result = ""
        # start
        for i in range(amount_of_pieces):
            result += f"/{'-' * self.horizontal_size}\\"
        if remains:
            result += f"/{'-' * remains}|"
        result += "\n"
        # body
        pieces = self.horizontal_size // len(self.farsh)
        body_string = self.farsh * (pieces) + self.farsh[0:self.horizontal_size - pieces * len(self.farsh)]
        for _ in range(3):
            for i in range(amount_of_pieces):
                result += f"|{body_string}|"
            if remains:
                result += f"|{body_string[0:remains]}|"
            result += "\n"
        # finish
        for i in range(amount_of_pieces):
            result += f"\{'-' * self.horizontal_size}/"
        if remains:
            result += f"\{'-' * remains}|"
        return result

    def __add__(self, other):
        _copy = copy.deepcopy(self)
        _copy.size += other.size
        return _copy

    def __sub__(self, other):
        _copy = copy.deepcopy(self)
        _copy.size -= other.size
        return _copy

    def __mul__(self, other):
        _copy = copy.deepcopy(self)
        _copy.size *= Fraction(other)
        return _copy

    def __rmul__(self, other):
        _copy = copy.deepcopy(self)
        _copy.size *= Fraction(other)
        return _copy

    def __truediv__(self, other):
        _copy = copy.deepcopy(self)
        _copy.size /= Fraction(other)
        return _copy

    def __bool__(self):
        if self.size > 0:
            return True
        else:
            return False
