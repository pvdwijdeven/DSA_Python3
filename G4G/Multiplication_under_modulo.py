class Solution:
    def multiplicationUnderModulo(self,a,b):
        md = 10**9 + 7
        return (a % md * b % md) % md

sol = Solution()
print(sol.multiplicationUnderModulo(92233720368547758,92233720368547758))
print(sol.multiplicationUnderModulo(1000000007,1000000007))

