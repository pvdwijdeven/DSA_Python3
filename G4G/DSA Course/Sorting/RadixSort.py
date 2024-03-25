# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.
def counting_sort(arr, exp) -> None:
    n = len(arr)
    # The output array elements that will have sorted arr
    output = [0] * (n)
    # initialize count array as 0
    count = [0] * (10)
    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] / exp
        count[int((index) % 10)] += 1
    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] / exp
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1
    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Method to do Radix Sort
def radix_sort(arr):
    # Find the maximum number to know number of digits
    max_item = max(arr)
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max_item // exp > 0:
        counting_sort(arr=arr, exp=exp)
        exp *= 10
    return arr


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print(radix_sort(arr=arr))
