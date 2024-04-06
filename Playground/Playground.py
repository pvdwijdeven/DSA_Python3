class Solution:

    # Function to check if two strings are rotations of each other or not.
    def areRotations(self, s1, s2):
        # code here
        n = len(s1)
        s_check = s1
        for i in range(n):
            if s_check == s2:
                return True
            s_check = s_check[1:] + s1[i]
        return False
