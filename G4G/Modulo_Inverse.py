class Solution:    
    ##Complete this function
    def modInverse(self,a,m):
        ##Your code here
        for x in range(1,m):
            if (x * a) % m == 1:
                return x
        return -1
    
sol = Solution()

print(sol.modInverse(3,11))
print(sol.modInverse(10,17))
    