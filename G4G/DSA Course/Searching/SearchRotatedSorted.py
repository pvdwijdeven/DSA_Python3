def search_rotated_sorted(arr, x) -> int:
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        if arr[low] < arr[mid]:
            if arr[low] <= x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


if __name__ == "__main__":
    arr = [5, 6, 7, 8, 9, 1, 2, 3, 4]
    x = 7
    print(search_rotated_sorted(arr=arr, x=x))
    arr = [5, 6, 7, 8, 9, 1, 2, 3, 4]
    x = 3
    print(search_rotated_sorted(arr=arr, x=x))
    arr = [5, 6, 7, 8, 9, 1, 2, 3, 4]
    x = 9
    print(search_rotated_sorted(arr=arr, x=x))
    arr = [5, 6, 7, 8, 9, 1, 2, 3, 4]
    x = 1
    print(search_rotated_sorted(arr=arr, x=x))
