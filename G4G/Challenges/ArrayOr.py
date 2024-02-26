class Solution:
    def game_with_number(self, arr, n):
        # Complete the function
        res = []
        for i, value in enumerate(iterable=arr):
            if i < n - 1:
                res.append(arr[i + 1] | value)
            else:
                res.append(value)
        return res


s = Solution()

print(s.game_with_number([5, 9, 2, 6], 4))
