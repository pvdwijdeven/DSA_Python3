class Solution:   
    def findPeakUtil(self,arr,low,high,n):
        # calculating mid
        mid=(low+high)//2
        # if mid is last or first index with first element
        # greater than next.
        # Also, check if mid element is greater than mid - 1 and mid+1
        if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid] ):
            return mid
        # If mid is other than 0, then check if mid element is less than prev.
        # If so, then recurse for lower half
        elif (mid>0 and arr[mid-1]>arr[mid]):
            return self.findPeakUtil(arr,low,mid-1,n)
        # else recurse for the upper half
        else :
            return self.findPeakUtil(arr,mid+1,high,n)
    def peakElement(self,arr, n):
        return self.findPeakUtil(arr,0,n-1,n)
    

sol = Solution()

arr = [2,7,2,2,2,2,2,2,2,2,2,2,2]
n = len(arr)

print(sol.peakElement(arr,n))