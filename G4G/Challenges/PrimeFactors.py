
from typing import List
from math import floor, sqrt

def get_list_of_primes(n):
    limit = n+1  # this is the 10000th prime
    if limit % 2 != 0:
        limit += 1
    primes_ = [True] * limit
    primes_[0], primes_[1] = [None] * 2
    for ind, val in enumerate(primes_):
        if val is True:
            # sieve out non-primes by multiples of known primes
            primes_[ind * 2::ind] = [False] * (((limit - 1) // ind) - 1)
    return primes_


def get_all_primes_to_limit(limit):
    primes_ = []
    sieve_list = get_list_of_primes(limit)
    for i in range(limit+1):
        if sieve_list[i]:
            primes_.append(i)
    return primes_

class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        primes = get_all_primes_to_limit(b+1)
        def prime_factors(n):
            ans = 0
            i = 0
            x = primes[i]
            while x * x <= n:
                if n % x:
                    i += 1
                    x = primes[i]
                else:
                    n //= x
                    ans +=1
            if n > 1:
                ans+=1
            return ans
        
        ans = 0
        for x in range(a,b+1):
            ans += prime_factors(x)
        return ans
    
sol = Solution()
print(sol.sumOfPowers(24,27))