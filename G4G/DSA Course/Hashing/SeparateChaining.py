
class Solution:
    
    #Function to insert elements of array in the hashTable avoiding collisions.
    def separateChaining(self, hashSize, arr, sizeOfArray):
        #Your code here
        #return hashtable
        hash  = [[] for x in range(hashSize)]
        for element in arr:
            key = element % hashSize
            hash[key].append(element)
        return hash
    
    
sol = Solution()
hashSize = 10
arr = [92,4,14,24,44,91]


print(sol.separateChaining(hashSize,arr,len(arr)))