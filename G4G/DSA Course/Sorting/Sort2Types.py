def sort_positive_negative(arr) -> None:
    i, j = -1, len(arr)
    while True:
        i += 1
        while arr[i] < 0:
            i += 1
        j -= 1
        while arr[j] >= 0:
            j -= 1
        if i >= j:
            return
        arr[i], arr[j] = arr[j], arr[i]


def sort_odd_even(arr) -> None:
    i, j = -1, len(arr)
    while True:
        i += 1
        while arr[i] % 2 == 0:
            i += 1
        j -= 1
        while arr[j] % 2 != 0:
            j -= 1
        if i >= j:
            return
        arr[i], arr[j] = arr[j], arr[i]


def sort_binary(arr) -> None:
    i, j = -1, len(arr)
    while True:
        i += 1
        while arr[i] == 0:
            i += 1
        j -= 1
        while arr[j] == 1:
            j -= 1
        if i >= j:
            return
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    arr = [-12, 18, -10, 15]
    sort_positive_negative(arr=arr)
    print(arr)
    arr = [5, 18, 10, 15]
    sort_odd_even(arr=arr)
    print(arr)
    arr = [1, 0, 1, 1, 1, 0, 1, 0, 1]
    sort_binary(arr=arr)
    print(arr)
