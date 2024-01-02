class Solution:
    def sumUnderModulo(self,a,b):
        md = 10**9 + 7
        return (a % md + b % md) % md

sol = Solution()
print(sol.sumUnderModulo(9223372036854775807,9223372036854775807))
print(sol.sumUnderModulo(1000000007,1000000007))

