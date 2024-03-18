# A Python program to find a peak element
# a peak is also a peak if on right or left side with neighbour lower.
def find_peak_recursive(arr) -> int:
    def find_peak_util(arr, left, right, n) -> int:
        # calculating mid
        mid = (left + right) // 2
        # if mid is last or first index with first element
        # greater than next.
        # Also, check if mid element is greater than mid - 1 and mid+1
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (
            mid == n - 1 or arr[mid + 1] <= arr[mid]
        ):
            return mid
        # If mid is other than 0, then check if mid element is less than prev.
        # If so, then recurse for lower half
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return find_peak_util(arr=arr, left=left, right=mid - 1, n=n)
        # else recurse for the upper half
        else:
            return find_peak_util(arr=arr, left=mid + 1, right=right, n=n)

    n = len(arr)
    return find_peak_util(arr=arr, left=0, right=n - 1, n=n)


# A Python program to find a peak element
# a peak is also a peak if on right or left side with neighbour lower.
def find_peak(arr) -> int:
    n = len(arr)
    left = 0
    right = n - 1
    mid = (left + right) // 2

    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (
            mid == n - 1 or arr[mid + 1] <= arr[mid]
        ):
            break
        if mid > 0 and arr[mid - 1] > arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return mid


if __name__ == "__main__":
    arr = [1, 3, 20, 4, 1, 0]
    print(find_peak(arr=arr))
    print(find_peak_recursive(arr=arr))
    arr = [5, 3, 1, 4, 5, 6]
    print(find_peak(arr=arr))
    print(find_peak_recursive(arr=arr))
    arr = [1, 2, 3, 4, 5, 6]
    print(find_peak(arr=arr))
    print(find_peak_recursive(arr=arr))