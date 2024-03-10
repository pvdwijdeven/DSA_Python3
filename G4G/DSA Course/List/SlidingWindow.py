# The following function gives the max sum of  subarray of K
# elements, using sliding window technique
def sliding_window(arr, K) -> int:
    n = len(arr)
    if n < K:
        return -1
    window_sum = sum(arr[:K])
    max_sum = window_sum
    for i in range(n - K):
        window_sum = window_sum - arr[i] + arr[i + K]
        max_sum = max(window_sum, max_sum)
    return max_sum


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr2 = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    arr3 = [1, 0]
    print(sliding_window(arr=arr1, K=3))
    print(sliding_window(arr=arr2, K=4))
    print(sliding_window(arr=arr3, K=3))
