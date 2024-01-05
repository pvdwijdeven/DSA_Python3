class Solution:
    def printArrayRecursively(self,arr,n):
        #code here
        if n==0:
            return
        self.printArrayRecursively(arr,n-1)
        print(arr[n-1], end = " ") 
    
sol = Solution()
n = 5
arr = [1,2,3,4,5]
sol.printArrayRecursively(arr,n)

