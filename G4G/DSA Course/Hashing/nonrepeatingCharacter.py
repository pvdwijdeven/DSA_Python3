#User function Template for python3

class Solution:
    
    #Function to find the first non-repeating character in a string.
    def nonrepeatingCharacter(self,s):
        #code here
        dict = {}
        for char in s:
            dict[char] = 0
        
        
        for char in s:
            dict[char] +=1
            
        for char in s:
            if dict[char] == 1:
                return char
        return "$"

sol = Solution()

print(sol.nonrepeatingCharacter("abcdabcddeefgha"))