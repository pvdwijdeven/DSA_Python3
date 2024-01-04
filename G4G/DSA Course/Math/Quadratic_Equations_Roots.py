from math import sqrt, floor


class Solution:
    def quadraticRoots(self, a, b, c):
        if b**2-4*a*c < 0: return [-1]
        return sorted([floor((-1*b + (sqrt(b**2-4*a*c)))/(2*a)),floor((-1*b - (sqrt(b**2-4*a*c)))/(2*a))], reverse=True)
    
sol = Solution()


try:
    assert sol.quadraticRoots(1,-2,1)==[1,1]
except AssertionError:
        print(sol.quadraticRoots(1,-2,1))
try:
    assert sol.quadraticRoots(1,-7,12)==[4,3]
except AssertionError:
        print(sol.quadraticRoots(1,-7,12))
try:
    assert sol.quadraticRoots(2,8,8)==[-2,-2]
except AssertionError:
        print(sol.quadraticRoots(2,8,8))
try:
    assert sol.quadraticRoots(280,399,573)==[-1]
except AssertionError:
        print(sol.quadraticRoots(280,399,573))
try:
    assert sol.quadraticRoots(-264,-750,504)==[0,-4]
except AssertionError:
        print(sol.quadraticRoots(-264,-750,504))
