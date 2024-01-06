class Solution:
    class Solution:
        def isPalin(self,N):
            n=str(N)
            #code here
            if len(n)<=1:
                return 1
            
            return ((n[0]==n[-1]) and self.isPalin(n[1:-1]))