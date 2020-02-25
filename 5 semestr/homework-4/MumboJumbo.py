def lexems_in_word(word):
    lexems = set(str(c) for c in word)
    return lexems


def mumbo_or_jumbo():
    first = word = input()
    is_even = False
    lexems_even = lexems_odd = set()  # lexems_in_each_alphabet
    while len(word) != 0:
        if is_even:
            lexems_even = lexems_even.union(lexems_in_word(word))
        else:
            lexems_odd = lexems_odd.union(lexems_in_word(word))
        word = input()
        is_even = not is_even  # next word changes parity
    if len(lexems_even) > len(lexems_odd):
        return "Jumbo"
    else:
        return "Mumbo"


print(mumbo_or_jumbo())


