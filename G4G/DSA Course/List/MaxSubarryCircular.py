# This function calculates the maximum sum of a
# subarray within the given circular array
def max_circular_subarray_sum(arr) -> int:
    n = len(arr)
    if n == 1:
        return arr[0]
    max_sum = arr[0]
    max_so_far = [arr[0]]
    min_sum = arr[0]
    min_so_far = [arr[0]]
    sum = arr[0]
    for i in range(1, n):
        max_so_far.append(max(arr[i], arr[i] + max_so_far[i - 1]))
        max_sum = max(max_sum, max_so_far[i])
        min_so_far.append(min(arr[i], arr[i] + min_so_far[i - 1]))
        min_sum = min(min_sum, min_so_far[i])
        sum += arr[i]
    if sum == min_sum:
        return max_sum
    return max(max_sum, sum - min_sum)


if __name__ == "__main__":
    arr1 = [8, -8, 9, -9, 10, -11, 12]
    arr2 = [-1, -2, -3, -4]
    arr3 = [10, -3, -4, 7, 6, 5, -4, -1]
    print(max_circular_subarray_sum(arr=arr1))
    print(max_circular_subarray_sum(arr=arr2))
    print(max_circular_subarray_sum(arr=arr3))
