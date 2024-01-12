def lomutoPartition(arr, l, h):
    pivot = arr[h]
    i = l - 1

    for j in range(l, h):
        if arr[j] <= pivot:  # error
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]

    return i + 1


def hoarsePartition(arr, l, h):
    pivot = arr[l]

    i = l - 1
    j = h + 1

    while True:

        i = i + 1
        while arr[i] < pivot:
            i = i + 1

        j = j - 1
        while arr[j] > pivot:
            j = j - 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]

def qSort(arr, l=0, h=None, partition = lomutoPartition):
    if h==None:
        h = len(arr)-1
    par = 0 if partition == hoarsePartition else 1
    if l < h:
        p = partition(arr, l, h)
        qSort(arr, l, p - par, partition)
        qSort(arr, p + 1, h, partition)


arr = [8, 4, 7, 9, 3, 10, 5]

qSort(arr,partition = hoarsePartition)

print(*arr)