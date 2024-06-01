def maxactivities(arr, overlap=True):
    n = len(arr)
    arr.sort(key=lambda x: x[1])
    prev = 0
    res = 1
    for curr in range(1, n):
        if overlap:
            if arr[curr][0] >= arr[prev][1]:
                res += 1
                prev = curr
        else:
            if arr[curr][0] > arr[prev][1]:
                res += 1
                prev = curr
    return res


class Solution:

    # Function to find the maximum number of activities that can
    # be performed by a single person.
    def activitySelection(self, n, start, end):
        arr = list(zip(start, end))
        return maxactivities(arr, False)


# {
# Driver Code Starts
# Initial Template for Python 3

import sys

start = [1, 3, 2, 5]
end = [2, 4, 3, 6]
n = end
ob = Solution()
print(ob.activitySelection(n, start, end))
