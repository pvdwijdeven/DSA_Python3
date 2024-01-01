from math import factorial
import timeit

# if possible always use math.factorial, is way faster and accepts higher numbers (recursive max depth = 995)

def factorial_recursive(N):
    if N == 0:
        return 1
    ans = N
    if N != 1:
        ans *= factorial_recursive(N-1) 
    return ans

print(factorial_recursive(100))
result = timeit.timeit(stmt='factorial_recursive(995)', globals=globals(), number=50)
print(result)
print(factorial(100))
result = timeit.timeit(stmt='factorial(995)', globals=globals(), number=50)
print(result)
