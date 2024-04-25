def guesser(n, guess) -> list[int]:
    res: list[int] = [-1] * n
    check1: int = guess(0, 1, "min")  # 1 1 2
    check2: int = guess(1, 2, "min")  # 2 1 1
    check3: int = guess(0, 2, "min")  # 1
    check4: int = guess(0, 1, "max")  # 2 3 3
    check5: int = guess(1, 2, "max")  # 3 3 3
    check6: int = guess(0, 2, "max")  # 3
    if check1 == check3:
        res[0] = check1
    elif check4 == check6:
        res[0] = check4
    elif check1 == check2:
        res[0] = check4
    elif check4 == check5:
        res[0] = check1
    res[1] = check1 if check1 != res[0] else check4
    res[2] = check3 if check3 != res[0] else check6
    for x in range(3, n):
        x_max: int = guess(x - 1, x, "max")
        y_max: int = guess(x - 1, x, "min")
        if x_max == res[x - 1]:
            res[x] = y_max
        else:
            res[x] = x_max
    return res


def guess(a: int, b: int, c: str) -> int:
    if c == "max":
        return max(lst[a], lst[b])
    else:
        return min(lst[a], lst[b])


test_lst: list[list[int]] = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
]
for lst in test_lst:
    res: list[int] = guesser(n=len(lst), guess=guess)
    print(res, res == lst)
