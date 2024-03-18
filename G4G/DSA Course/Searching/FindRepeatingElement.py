# the following function finds the repeating number in O(n) time and O(1) space
def find_repeating_element(arr,) -> int:
    # add 1 to calculation, in case 0 is used in array
    extra = 1

    slow = arr[0] + extra
    fast = arr[0] + extra
    slow = arr[slow] + extra
    fast = arr[arr[fast]] + extra
    while slow != fast:
        slow = arr[slow] + extra
        fast = arr[arr[fast]] + extra
    slow = arr[0] + extra
    while slow != fast:
        slow = arr[slow] + extra
        fast = arr[fast] + extra
    return slow - extra


if __name__ == "__main__":
    arr = [0, 3, 2, 4, 6, 5, 7, 3]
    print(find_repeating_element(arr=arr))