class Solution:
    def isSorted(self,arr,n):
        reversed = arr[0] > arr[-1]
        prev = arr[0]
        for x in range(1,len(arr)):
            if reversed:
                if arr[x] > prev: return 0
            else:
                if arr[x] < prev: return 0
            prev = arr[x]
        return 1


sol = Solution()

print(sol.isSorted([1,1,2,2,3],5))
print(sol.isSorted([4,2],2))