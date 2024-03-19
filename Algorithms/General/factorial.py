from math import factorial
import timeit

# if possible always use math.factorial, is way faster and accepts higher numbers (recursive max depth)
def factorial_recursive(N):
    if N == 0:
        return 1
    if N != 1:
        N *= factorial_recursive(N-1) 
    return N

def factTR(N, a): #slowest!!!
    if (N == 0):  
        return a 

    return factTR(N-1, N*a)

#print(factTR(10,1))

#print(factorial_recursive(100))
result = timeit.timeit(stmt='factTR(992, 1)', globals=globals(), number=500)
print(result)
result = timeit.timeit(stmt='factorial_recursive(992)', globals=globals(), number=500)
print(result)

#print(factorial(100))
result = timeit.timeit(stmt='factorial(992)', globals=globals(), number=500)
print(result)

