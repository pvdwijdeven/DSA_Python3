class Solution:
    def repeatedRows(self, arr, m ,n):
        result = []
        duplicates = []
        
        for i in range(m):
            if arr[i] in duplicates:
                result.append(i)
            
            else:
                duplicates.append(arr[i])
        
        return result
            
    
    
sol = Solution()


arr = [[ 1, 0, 0],
            [ 1, 0, 0],
            [ 0, 0, 0],
            [ 0, 0, 0]]

m = len(arr)
n = len(arr[0])

print(sol.repeatedRows(arr,m,n))