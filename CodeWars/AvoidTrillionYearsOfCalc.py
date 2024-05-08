from math import factorial


def fa(iterable):  # iterable, a string or an array
    return factorial(len(iterable)) + factorial(len(iterable) - 1)


print(fa("abc"))
