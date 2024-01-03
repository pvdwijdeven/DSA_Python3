#User function Template for python3
from math import sqrt, floor
class Solution:
    def isPrime(self,N):
        if N == 1:
            return False
        if N <= 3:
            return True
        
        if N % 2 == 0 or N % 3 == 0:
            return False
        top = floor(sqrt(N))
        
        for i in range(5,top+1,6):
            if N % i == 0 or N % (i+2) == 0:
                return False
        
        return True