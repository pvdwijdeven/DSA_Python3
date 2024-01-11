class Solution:
    def insert(self, alist, index, n):
        #code here
        for i in range(index-1,-1,-1):
            if alist[i] > alist[index]:
                alist[index],alist[i]=alist[i],alist[index]
                index = i
            else:
                return alist
        return alist

        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for i in range(0,n):
            alist = self.insert(alist,i,n)
        return alist
    
    
sol = Solution()

arr = [4,3,5,7,2,1,6]
n = len(arr)

print(sol.insertionSort(arr,n))

