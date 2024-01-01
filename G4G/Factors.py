#User function Template for python3

class Solution:
    #You need to complete this function
    def factorial(self,N):
        if N == 0:
            return 1
        ans = N
        if N != 1:
            ans *= self.factorial(N-1) 
        return ans
    
sol = Solution()

print(sol.factorial(100))
