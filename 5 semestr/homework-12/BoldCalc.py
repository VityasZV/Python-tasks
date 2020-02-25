from collections import Counter
class Calculator:
    def __init__(self):
        self.variables = dict()
        self.variables['__builtins__'] = dir(__builtins__)
        self.globals = {}
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        print(alphabet)
        cmd = input()
        l = []
        while cmd != "." and cmd != "":
            l.append(cmd)
            cmd = input()
        for i in l:
            try:
                if i.__contains__("="):
                    arg = i[0:i.find("=")]
                    res = i[i.find("=") + 1:len(i)]
                    if arg[0] not in alphabet:
                        raise SyntaxError(f"invalid identifier \'{arg}\'")
                    elif Counter(i)['='] != 1:
                        raise SyntaxError(f"invalid assignment \'{i}\'")
                    else:
                        self.variables[arg] = eval(res, self.globals, self.variables)
                elif i[0] == '#':
                    continue
                else:
                    print(eval(i, self.globals, self.variables))
            except BaseException as Ex:
                print(Ex)
Calculator()
