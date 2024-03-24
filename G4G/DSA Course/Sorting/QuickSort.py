def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def hoare_partition(arr, low, high):
    pivot = arr[(high + low) // 2]
    i = low
    j = high

    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def qSort(arr, low=0, high=None, partition=lomuto_partition):
    if high is None:
        high = len(arr) - 1
    par = 0 if partition == hoare_partition else 1
    if low < high:
        p = partition(arr, low, high)
        qSort(arr=arr, low=low, high=p - par, partition=partition)
        qSort(arr=arr, low=p + 1, high=high, partition=partition)


def qSort_optimized(arr, low=0, high=None, partition=lomuto_partition):
    if high is None:
        high = len(arr) - 1
    par = 0 if partition == hoare_partition else 1
    while low < high:
        p = partition(arr, low, high)
        qSort_optimized(arr=arr, low=low, high=p - par, partition=partition)
        low = p + 1


if __name__ == "__main__":
    arr = [8, 4, 7, 9, 3, 10, 5]
    qSort(arr=arr, partition=hoare_partition)
    print(*arr)
    arr = [8, 4, 7, 9, 3, 10, 5]
    qSort(arr=arr, partition=lomuto_partition)
    print(*arr)
    arr = [8, 4, 7, 9, 3, 10, 5]
    qSort_optimized(arr=arr, partition=hoare_partition)
    print(*arr)
    arr = [8, 4, 7, 9, 3, 10, 5]
    qSort_optimized(arr=arr, partition=lomuto_partition)
    print(*arr)
