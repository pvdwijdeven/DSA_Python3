
class Solution:
    def fibonacci(self,n):
        #code here
        if n==1:
            return 1
        if n==2:
            return 1
        return self.fibonacci(n-1) + self.fibonacci(n-2)
        
sol = Solution()
print(sol.fibonacci(20))
