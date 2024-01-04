import math


class Solution:    
    #Compelte his function
    def termOfGP(self,A,B,N):
        return(A*(B/A)**(N-1))

sol = Solution()

try:
    assert sol.termOfGP(2,3,1)==2
except AssertionError:
        print(sol.termOfGP(2,3,1))
try:
    assert sol.termOfGP(1,2,5)==16
except AssertionError:
        print(sol.termOfGP(1,2,5))
try:
    assert sol.termOfGP(84,87,3)==90
except AssertionError:
        print(sol.termOfGP(85,87,3))