# Python code to implement the approach
import math


# Function to decide who should play first
def game(self, A, B):
    # code here
    diff = abs(B - A)
    d = int(((1 + math.sqrt(5)) / 2) * diff)
    if d == min(A, B):
        return False
    else:
        return True
