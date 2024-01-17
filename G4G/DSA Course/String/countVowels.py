
class Solution:
    def countVowels_distinct(self,s):
        #code here
        total = 0
        vowels = "aeoiu"
        for char in vowels:
            if char in s:
                total+=1
        return total

    def countVowels(self,s):
        #code here
        total = 0
        vowels = "aeoiu"
        for char in s:
            if char in vowels:
                total+=1
        return total

    
sol = Solution()
s="hyena"
print(sol.countVowels(s))