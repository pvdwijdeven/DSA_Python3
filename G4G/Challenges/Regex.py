import re

class Solution:
    def search(self, pat, txt):
        # code here
        res = re.finditer(pat, txt)
        ans=[]

        for match in res:
            ans.append(match.start()+1)
        if ans==[]:
            return -1
        return ans
    
sol = Solution()
print(sol.search('geek','geeks4geeks'))