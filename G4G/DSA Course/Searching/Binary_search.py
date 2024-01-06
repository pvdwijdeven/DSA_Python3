class Solution:
    ##Complete this function
    def searchInSorted(self,arr, N, K):
        #Your code here
        low = 0
        high = len(arr)-1

        while low <= high:
            mid = low + (high-low)//2
            if arr[mid]==K:
                return mid
            elif arr[mid]<K:
                low = mid+1
            else:
                high = mid-1
        return -1
    
sol=Solution()
print(sol.searchInSorted([1,2,3,4,6],5,6))