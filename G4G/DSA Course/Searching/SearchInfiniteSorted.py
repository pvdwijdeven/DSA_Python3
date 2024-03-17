def binary_search(arr, x) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def search_infinite_sorted(arr, x) -> int:
    if arr[0] == x:
        return 0
    i = 1
    if arr[i] == x:
        return 1
    while arr[i] < x:
        i = i * 2
        if arr[i] == x:
            return i
        if arr[i] > x:
            return i // 2 + 1 + binary_search(arr=arr[i // 2 + 1 : i], x=x)
    return -1


if __name__ == "__main__":
    arr = [*range(0, 10**6)]
    arr += [10**9 + 1] * 10**6
    x = 99999
    print(search_infinite_sorted(arr=arr, x=x))
