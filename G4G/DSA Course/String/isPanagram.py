class Solution:
    def isPanagram(self,s):
        #your code here
        h = [0 for x in range(26)]
        for char in s:
            if ord(char)>=97:
                h[ord(char)-97]+=1
            else:
                h[ord(char)-65]+=1
        for count in h:
            if  count==0: return False
        return True              
                
