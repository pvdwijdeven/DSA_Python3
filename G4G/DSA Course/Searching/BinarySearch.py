def binary_search(arr, x) -> int:
    # Your code here
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


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6]
    x = 6
    print(binary_search(arr=arr, x=x))
    arr = range(0, 10**9)
    x = 99999
    print(binary_search(arr=arr, x=x))
