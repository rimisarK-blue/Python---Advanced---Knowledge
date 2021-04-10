from functools import reduce


def operate(a, *args):
    return reduce(lambda x, y : eval(f"{x} {a} {y}"), args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
