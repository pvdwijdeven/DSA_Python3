# Function to rotate an array by d elements using slicing
def rotate_array_slicing(arr, d, direction="left") -> list:
    if direction == "left":
        arr = arr[d:] + arr[:d]
    else:
        arr = arr[len(arr) - d :] + arr[: len(arr) - d]
    return arr


# Function to rotate an array by d elements using dque
def rotate_array_dque(arr, d, direction="left") -> list:
    from collections import deque

    d = -d if direction == "left" else d
    arr = deque(arr)
    arr.rotate(d)
    return list(arr)


# Function to rotate an array by d elements using pop and append
def rotate_array_pop_append(arr, d, direction="left") -> list:
    res = arr[:]
    if direction == "left":
        for _ in range(0, d):
            res.append(res.pop(0))
    else:
        for _ in range(0, len(res) - d):
            res.append(res.pop(0))
    return res


# Function to rotate an array by d elements using reversing
def rotate_array_reverse(arr, d, direction="left") -> list:

    def reverse(arr, begin, end) -> None:
        while begin < end:
            arr[begin], arr[end] = arr[end], arr[begin]
            begin = begin + 1
            end = end - 1

    res = arr[:]
    n = len(res)
    if direction == "left":
        reverse(arr=res, begin=0, end=d - 1)
        reverse(arr=res, begin=d, end=n - 1)
        reverse(arr=res, begin=0, end=n - 1)
    else:
        reverse(arr=res, begin=0, end=n - d - 1)
        reverse(arr=res, begin=n - d, end=n - 1)
        reverse(arr=res, begin=0, end=n - 1)
    return res


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print(rotate_array_slicing(arr=arr1, d=2))
    print(rotate_array_slicing(arr=arr2, d=3))
    print(rotate_array_slicing(arr=arr2, d=3, direction="right"))
    print(rotate_array_dque(arr=arr1, d=2))
    print(rotate_array_dque(arr=arr2, d=3))
    print(rotate_array_dque(arr=arr2, d=3, direction="right"))
    print(rotate_array_pop_append(arr=arr1, d=2))
    print(rotate_array_pop_append(arr=arr2, d=3))
    print(rotate_array_pop_append(arr=arr2, d=3, direction="right"))
    print(rotate_array_reverse(arr=arr1, d=2))
    print(rotate_array_reverse(arr=arr2, d=3))
    print(rotate_array_reverse(arr=arr2, d=3, direction="right"))
