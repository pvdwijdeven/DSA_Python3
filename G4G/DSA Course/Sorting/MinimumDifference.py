# Chocolate Distribution Problem
# Give to m children an amount of boxes as per array,
# in such a way that the difference is mimimal


def minimum_difference(arr, m) -> int:
    if m == 0 or len(arr) == 0:
        return 0
    if len(arr) < m:
        return -1
    arr.sort()
    res = arr[m - 1] - arr[0]
    for i in range(1, len(arr) - m + 1):
        res = min(res, abs(arr[i + m - 1] - arr[i]))
    return res


if __name__ == "__main__":
    arr = [7, 3, 1, 8, 9, 12, 56]
    print(minimum_difference(arr=arr, m=3))
