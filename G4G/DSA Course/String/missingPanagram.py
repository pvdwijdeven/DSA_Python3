class Solution:
    def missingPanagram(self,s):
        #your code here
        res = ""
        h = [0 for x in range(26)]
        for char in s:
            if ord(char)>=97:
                h[ord(char)-97]+=1
            else:
                h[ord(char)-65]+=1
        for count in range(26):
            if  h[count]==0:
                res += chr(count)
        return res              
                