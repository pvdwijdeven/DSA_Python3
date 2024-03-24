def lomuto_partition(arr, low, high) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def kth_smallest(arr, k) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        pivot = lomuto_partition(arr=arr, low=low, high=high)
        if pivot == k - 1:
            return arr[pivot]
        elif pivot > k - 1:
            high = pivot - 1
        else:
            low = pivot + 1
    return -1


if __name__ == "__main__":
    arr = [10, 4, 5, 8, 6, 26]
    k = 3
    print(kth_smallest(arr=arr, k=k))
