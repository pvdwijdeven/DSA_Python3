#User function Template for python3
from math import floor, log
class Solution:
    def digitsInFactorial(self,N):
        if N < 0:return 0
        if N <= 1: return 1
        digits = 0 
        for x in range(2, N+1):
            digits += log(x, 10) 
        return floor(digits)+1
    
    
sol = Solution()

print(sol.digitsInFactorial(10**9))