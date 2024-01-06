class Solution:
    def GCD(self,a,b):
        #code here
        if b!=0:
            return self.GCD(b, a%b)
        else:
            return a

sol = Solution()
print(sol.GCD(15,5))