class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        low = 0
        high = len(A)-1

        while low <= high:
            mid = low + (high-low)//2
            if A[mid]<=X and mid==N-1:
                return mid
            elif A[mid]==X:
                return mid
            elif A[mid]<X and A[mid+1]>X:
                return mid
            elif A[mid]<X:
                low = mid+1
            else:
                high = mid-1
        return -1     

sol=Solution()
A=[1,2,8,10,11,12,19]
N=len(A)
X=0

print(sol.findFloor(A,N,X))

A=[1,2,8,10,11,12,19]
N=len(A)
X=5

print(sol.findFloor(A,N,X))