#User function Template for python3

class Solution:
    #Function to fill the array elements into a hash table 
    #using Linear Probing to handle collisions.
    
    def QuadraticProbing(self,hash, hashSize, arr, sizeOfArray):
        #Your code here
        size = hashSize
        hash = [-1] * hashSize
        for element in arr:
            if element in hash:
                continue
            done = False
            plus = 0
            while not done:
                pos = (element+plus**2) % hashSize
                if hash[pos] == -1:
                    hash[pos] = element
                    size -= 1
                    done = True
                    if size == 0 : 
                        return hash
                else:
                    plus +=1
        return hash
    
sol = Solution()
hash=[]

arr = [21,10,32,43]
hashSize = 11
print(sol.QuadraticProbing(hash, hashSize,arr,len(arr)))