# User function Template for python3


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


_MIN = -2147483648
_MAX = 2147483648


# Function to return the maximum difference between any node and its ancestor.
def maxDiffUtil(t, res):
    """Returning Maximum value if node
    is not there (one child case)"""
    if t == None:
        return _MAX, res

    """ If leaf node then just return
        node's value """
    if t.left == None and t.right == None:
        return t.data, res

    """ Recursively calling left and right 
    subtree for minimum value """
    a, res = maxDiffUtil(t.left, res)
    b, res = maxDiffUtil(t.right, res)
    val = min(a, b)

    """ Updating res if (node value - minimum 
    value from subtree) is bigger than res """
    res = max(res, t.data - val)

    """ Returning minimum value got so far """
    return min(val, t.data), res

    """ This function mainly calls maxDiffUtil() """


def maxDiff(root):

    # Initialising result with minimum value
    res = _MIN
    x, res = maxDiffUtil(root, res)
    return res


""" Helper function to print inorder
traversal of binary tree """


def inorder(root):

    if root:

        inorder(root.left)
        print("%d ", root.data)
        inorder(root.right)
