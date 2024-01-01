from math import sqrt
from functools import reduce
import timeit

def factors(n):
    # works deeper and way faster than recursive function!
    step = 2 if n % 2 else 1
    return sorted(list(set(reduce(list.__add__,
                                  ([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))))


def factorial_recursive(N):
    # don't use...
    if N == 0:
        return 1
    ans = N
    if N != 1:
        ans *= factorial_recursive(N-1) 
    return ans

def prime_factors(n):
    i = 2
    prime_factor_list = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factor_list.append(i)
    if n > 1:
        prime_factor_list.append(n)
    return prime_factor_list


print(factors(10**9))
result = timeit.timeit(stmt='factors(10**2)', globals=globals(), number=50)
print(result)
print(factorial_recursive(10**2))
result = timeit.timeit(stmt='factorial_recursive(10**2)', globals=globals(), number=50)
print(result)
print(prime_factors(10**9))