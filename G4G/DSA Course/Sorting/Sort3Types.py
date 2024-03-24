# Sort an array with three types of elements
def sort_3_types(arr) -> list[int]:
    low, mid, high = 0, 0, (len(arr) - 1)
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr


if __name__ == "__main__":
    arr = [0, 1, 2, 1, 0, 0]
    print(sort_3_types(arr=arr))
