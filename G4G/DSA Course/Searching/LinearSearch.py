

class Solution:
    #Complete the below function
    def search(self,arr, N, X):
        #Your code here


        left = 0
        length = len(arr)
        position = -1
        right = length - 1

        # Run loop from 0 to right
        for left in range(0, right, 1):
            #If search_element is found with
            # left variable
            if (arr[left] == X):
                position = left
                return position
                break

            # If search_element is found with# right variable
            if (arr[right] == X):
                position = right
                return position
                break
            left += 1
            right -= 1

        # If element not found
        return -1
            
sol=Solution()

arr=[1,2,3,4,5]
N=len(arr)
X=5

print(sol.search(arr,N,X))