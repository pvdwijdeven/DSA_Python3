def smaller_than_x(arr, x) -> int:
    ans = 0
    for i in arr:
        if i < x:
            ans += 1
    return ans


def immediate_smaller(arr, x) -> int:
    min_diff = x
    ans = -1
    for i in arr:
        if i < x and x - i < min_diff:
            min_diff = x - i
            ans = i
    return ans


def greater_than_x(arr, x) -> int:
    ans = 0
    for i in arr:
        if i > x:
            ans += 1
    return ans


def immediate_greater(arr, x) -> int:
    min_diff = 10**6
    ans = -1
    for i in arr:
        if i > x and i - x < min_diff:
            min_diff = i - x
            ans = i
    return ans


def majorityWins(arr, x, y) -> int:
    c_x = 0
    c_y = 0
    for i in arr:
        if i == x:
            c_x += 1
        if i == y:
            c_y += 1
    if c_x > c_y:
        return x
    if c_x == c_y:
        return min(x, y)
    return y


if __name__ == "__main__":
    print(smaller_than_x(arr=[4, 5, 3, 1, 2], x=3))
    print(smaller_than_x(arr=[2, 2, 2, 2, 2, 2], x=3))

    print(immediate_smaller(arr=[4, 67, 13, 12, 15], x=16))
    print(immediate_smaller(arr=[1, 2, 3, 4, 5], x=1))

    print(greater_than_x(arr=[4, 5, 3, 1, 2], x=3))
    print(greater_than_x(arr=[2, 2, 2, 2, 2, 2], x=3))

    print(immediate_greater(arr=[4, 67, 13, 12, 15], x=16))
    print(immediate_greater(arr=[1, 2, 3, 4, 5], x=1))

    print(majorityWins(arr=[1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5], x=4, y=5))
    print(majorityWins(arr=[1, 2, 3, 4, 5, 6, 7, 8], x=1, y=7))
