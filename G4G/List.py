class Solution:
    def smallerThanX(self,arr,n,x):
        #return required ans
        ans = 0
        for i in arr:
            if i<x: ans+=1
        return ans
    
    def immediateSmaller(self,arr,n,x):
        #return required ans
        min_diff = x
        ans = -1
        for i in arr:
            if i<x and x-i<min_diff:
                min_diff = x-i
                ans = i
        return ans

    def greaterThanX(self,arr,n,x):
        #return required result
        ans = 0
        for i in arr:
            if i>x: ans+=1
        return ans
    
    def immediateGreater(self,arr,n,x):
        #return required ans
        min_diff = 10**6
        ans = -1
        for i in arr:
            if i>x and i-x<min_diff:
                min_diff = i-x
                ans = i
        return ans
    
    def majorityWins(self, arr, n, x, y):
        # code here
        c_x = 0
        c_y = 0
        for i in arr:
            if i == x: c_x+=1
            if i == y: c_y+=1
        if c_x > c_y: return x
        if c_x == c_y: return min(x,y)
        return y
            
            
            
sol = Solution()

print(sol.smallerThanX([4,5,3,1,2],5,3))
print(sol.smallerThanX([2,2,2,2,2,2],6,3))

print(sol.immediateSmaller([4,67,13,12,15],5,16))
print(sol.immediateSmaller([1,2,3,4,5],5,1))

print(sol.greaterThanX([4,5,3,1,2],5,3))
print(sol.greaterThanX([2,2,2,2,2,2],6,3))

print(sol.immediateGreater([4,67,13,12,15],5,16))
print(sol.immediateGreater([1,2,3,4,5],5,1))

print(sol.majorityWins([1,1,2,2,3,3,4,4,4,4,5],11,4,5))
print(sol.majorityWins([1,2,3,4,5,6,7,8],8,1,7))