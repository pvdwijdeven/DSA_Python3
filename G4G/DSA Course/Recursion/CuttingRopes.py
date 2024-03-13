# the following function shows the maximum cuts in a rope of
# length n, where only sizes a, b and/or c can be cut.
def cutting_ropes(length, a, b, c) -> int:
    if length < 0:
        return -1
    if length == 0:
        return 0
    res = max(
        cutting_ropes(length=length - a, a=a, b=b, c=c),
        cutting_ropes(length=length - b, a=a, b=b, c=c),
        cutting_ropes(length=length - c, a=a, b=b, c=c),
    )
    if res == -1:
        return -1
    return res + 1


if __name__ == "__main__":
    length, a, b, c = 23, 11, 9, 12
    print(cutting_ropes(length=length, a=a, b=b, c=c))
    length, a, b, c = 10, 2, 1, 5
    print(cutting_ropes(length=length, a=a, b=b, c=c))
