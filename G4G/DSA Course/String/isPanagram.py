class Solution:
    def isPanagram(self, s):
        # your code here
        h = [0 for x in range(26)]
        for char in s:
            char = char.lower()
            if char.isalnum()():
                h[ord(char) - 97] += 1
        for count in h:
            if count == 0:
                return False
        return True
