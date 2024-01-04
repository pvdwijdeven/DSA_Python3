class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        #Your code here
        A[:]= A[D:]+A[:D]
        return A

sol = Solution()

print(sol.rotateArr([1,2,3,4,5],2,5))
print(sol.rotateArr([2,4,6,8,10,12,14,16,18,20],3,10))