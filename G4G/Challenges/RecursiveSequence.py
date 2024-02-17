from sys import setrecursionlimit

setrecursionlimit(3 * 10**3)
from functools import lru_cache


@lru_cache(None)
class Solution:
    def sequence(self, n):
        # code here
        def rec(n, start, num):
            ans = start
            for x in range(start + 1, start + num):
                ans *= x % (10**9 + 7)
            if n != num:
                return ans + rec(n, start + num, num + 1)
            else:
                return ans

        return rec(n, 1, 1) % (10**9 + 7)


sol = Solution()

print(sol.sequence(997))
