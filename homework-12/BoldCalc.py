from collections import Counter
class Calculator:
    def __init__(self):
        self.variables = dict()
        self.variables['__builtins__'] = dir(__builtins__)
        alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
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
                        # print("debug:", res, type(res))
                        self.variables[arg] = eval(res, {'__builtins__': dir(__builtins__)}, self.variables)
                elif i[0] == '#':
                    continue
                else:
                    print(eval(i, {'__builtins__': dir(__builtins__)}, self.variables))
            except SyntaxError as Ex:
                print(Ex)
            except NameError as Ex:
                print(Ex)
            except TypeError as Ex:
                print(Ex)
            except BaseException as Ex:
                print(Ex)
        # print(self.variables)


c = Calculator()
