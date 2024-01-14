#User function Template for python3
class Solution:
    
    #Complete this function
    #Function to return non-repeated elements in the array.
    def printNonRepeated(self,arr,n):
        #Your code here
        dict={}
        
        for i in arr:
            dict[i]=0
        
        #storing the frequency of each element.
        for i in arr:
            dict[i]+=1
        res = []
        
        #iterating over the array elements.
        for i in arr:
            
            #if frequency of current element is 1,
            #then we increment the counter.
            if dict[i]==1:
                res.append(i)
                
        #returning the count of non-repeated elements.
        return res

sol = Solution()

arr = [1,2,3,4,5,1,1,2,3]

print(sol.printNonRepeated(arr,len(arr)))