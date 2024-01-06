class Solution:
    def leftIndex (self, N, arr, X):
        # code here 
        low = 0
        high = len(arr)-1

        while low <= high:
            mid = low + (high-low)//2
            if arr[mid]==X and (mid==0 or arr[mid-1]!=X):
                return mid
            elif arr[mid]<X:
                low = mid+1
            else:
                high = mid-1
        return -1
    
sol = Solution()
N=6
arr=[1,1,2,2,2,3,3,3,3,4,4,5,5,5]
X = 0

print(sol.leftIndex(N,arr,X))