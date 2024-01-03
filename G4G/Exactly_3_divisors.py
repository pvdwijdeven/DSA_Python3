#User function Template for python3
from math import floor, sqrt

def isPrime(N):
    if (N<= 1): return False
    elif (N<= 3): return True
    elif (N%2 == 0 or N%3 == 0): return False

    i = 5
    while i*i<=N:
        if (N%i==0 or N%(i+2)==0): return False
        i += 6

    return True

class Solution:
    def exactly3Divisors(self, N):
        total = 0
        for x in range (2,floor(sqrt(N))+1):
            if isPrime(x):
                total+=1
        return total