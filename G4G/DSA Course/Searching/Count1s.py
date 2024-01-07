
class Solution:
    ##Complete this code
    def countOnes(self,arr, N):
        #Your code here
        low = 0
        high = len(arr)-1

        while low <= high:
            mid = low + (high-low)//2
            if (mid == len(arr)-1 and arr[mid]==1) or (arr[mid]==1 and (mid==0 or arr[mid+1]!=1)):
                return mid+1
            elif arr[mid]<1:
                high = mid-1
            else:
                low = mid+1
        return 0
    
sol=Solution()

arr = [1,1,1,1,1,1,1,1,1]
N = len(arr)
print(sol.countOnes(arr,N))
