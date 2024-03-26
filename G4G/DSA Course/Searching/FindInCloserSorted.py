# Function to find index of element x in the array if it is present.
# Closer Sorted: first the array is sorted, but after sorting
# some elements are moved to either of the adjacent positions,
# i.e, maybe to the arr[i+1] or arr[i-1].
def find_in_closer_sorted(arr, x) -> int:
    low = 0
    n = len(arr)
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif mid + 1 <= n and arr[mid + 1] == x:
            return mid + 1
        elif mid - 1 >= 0 and arr[mid - 1] == x:
            return mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    arr = [3, 2, 10, 4, 40]
    x = 2
    print(find_in_closer_sorted(arr=arr, x=x))
