class Solution:
    def smallestSubstring(self, S):
        min_len = len(S)*2
        pos=[-1,-1,-1]
        
        for i,x in enumerate(S):
            if x == '0':
                pos[0] = i
            elif x == '1':
                pos[1] = i
            elif x == '2':
                pos[2] = i
            if -1 not in pos:
                cur_len = max(pos)-min(pos)+1
                if cur_len < min_len:
                    min_len = cur_len
        if min_len < len(S)+1:
            return min_len
        else:
            return -1
        
        
sol = Solution()

print(sol.smallestSubstring('012232'))
print(sol.smallestSubstring('032232'))
print(sol.smallestSubstring('01112232'))