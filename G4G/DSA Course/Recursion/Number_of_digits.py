class Solution:
    def countDigits(self, n):
        '''
        :param n: given number
        :return: sum of digits of n.
        '''
        if n == 0:
            return 0
        return (1 + self.countDigits(n // 10))

        
sol = Solution()
print(sol.countDigits(1234))