class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    # Function to return the maximum sum of non-adjacent nodes.
    def max_sum(self, root):
        if not root:
            return 0, 0

        no_root_l, root_l = self.max_sum(root.left)
        no_root_r, root_r = self.max_sum(root.right)

        root_sum_max = max(
            root.data,
            root.data + no_root_l,
            root.data + no_root_r,
            root.data + no_root_r + no_root_l,
        )
        no_root_sum_max = max(
            root_l,
            root_r,
            root_l + root_r,
            no_root_l + no_root_r,
            root_l + no_root_r,
            root_r + no_root_l,
        )

        return no_root_sum_max, root_sum_max

    def getMaxSum(self, root):
        return max(self.max_sum(root))
