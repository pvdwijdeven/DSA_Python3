#User function Template for python3

from math import sqrt, floor

class Solution:
    def quadraticRoots(self, a, b, c):
        if b**2-4*a*c < 0: return [-1]
        return sorted([floor((-1*b + (sqrt(b**2-4*a*c)))/(2*a)),floor((-1*b - (sqrt(b**2-4*a*c)))/(2*a))], reverse=True)


