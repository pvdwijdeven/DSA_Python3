#User function Template for python3

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        
        #arr : given array
        #n : size of the array
        dict = {}
        for element in arr:
            dict[element] = 0
        for element in arr:
            if dict[element] != 0:
                return element
            else:
                dict[element]+=1
        return -1



sol = Solution()

arr = [1,1,2,3,1,42,4,2,]
print(sol.firstRepeated(arr,len(arr)))