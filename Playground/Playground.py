class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class Solution:
    # Function to construct binary tree from parent array.
    def createTree(self, parent, N):
        hash = {}
        for i in range(N):
            if parent[i] not in hash:
                hash[parent[i]] = [i]
            else:
                hash[parent[i]].append(i)
        print(hash)


s = Solution()
arr = [-1, 0, 0, 1, 1, 3, 5]
s.createTree(arr, len(arr))
