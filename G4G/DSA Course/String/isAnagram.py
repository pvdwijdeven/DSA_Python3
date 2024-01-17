#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        h = [0 for x in range(65,122)]
        if len(a) == len(b):
            for i in range(len(a)):
                h[ord(a[i])-66]+=1
                h[ord(b[i])-66]-=1
        else:
            return False
        for i in h:
            if i != 0:
                return False
        return True
    

sol = Solution()
a = 'abzdef'
b = 'deaabc'
print(sol.isAnagram(a,b))
        