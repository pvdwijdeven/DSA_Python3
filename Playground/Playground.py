class Solution:
    # Function to find the length of longest subarray of even and odd numbers.
    def maxEvenOdd(self, arr, n) -> int:
        res = 0
        cur = 1
        is_even = [arr[0] % 2 == 0]
        for i in range(1, n):
            is_even.append(arr[i] % 2 == 0)
            if is_even[i] != is_even[i - 1]:
                cur += 1
            else:
                res = max(res, cur)
                cur = 1
        res = max(res, cur)
        return res


if __name__ == "__main__":
    s = Solution()
    arr1 = [10, 12, 14, 7, 8]
    arr2 = [4, 6]
    print(s.maxEvenOdd(arr=arr1, n=len(arr1)))
    print(s.maxEvenOdd(arr=arr2, n=len(arr2)))
