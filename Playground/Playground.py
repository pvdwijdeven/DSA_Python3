from collections import defaultdict


class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, A, B, N):
        mp = defaultdict(int)
        for i in range(len(A)):
            mp[A[i]] += 1
            mp[B[i]] -= 1
        for x in mp:
            if mp[x] != 0:
                return False
        return True
