# This function calculates the maximum sum of a
# subarray within the given array
def max_subarray_sum(arr) -> int:
    n = len(arr)
    res = arr[0]
    max_so_far = [arr[0]]
    for i in range(1, n):
        max_so_far.append(max(arr[i], arr[i] + max_so_far[i - 1]))
        res = max(res, max_so_far[i])
    return res


if __name__ == "__main__":
    arr1 = [1, 2, 3, -2, 5]
    arr2 = [-1, -2, -3, -4]
    print(max_subarray_sum(arr=arr1))
    print(max_subarray_sum(arr=arr2))
