class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        for i in range(n):
            swapped = False
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    swapped = True
                    arr[j],arr[j+1] = arr[j+1], arr[j]
            if not swapped: 
                return arr
        return arr
    
    
sol = Solution()
arr = [4, 1, 3, 9, 7]
# arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(sol.bubbleSort(arr,len(arr)))