class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to return a list containing the preorder traversal of the tree.
def isIdentical(root1, root2):
    # code here
    res = True

    if root1 != None and root2 != None:
        if root1.data != root2.data:
            return False
        res = isIdentical(root1.left, root2.left)
        res = res and isIdentical(root1.right, root2.right)
    else:
        if root1 != root2:
            return False
    return res


root1 = Node(1)
root1.left = Node(4)  # type: ignore
root1.left.left = Node(4)  # type: ignore
root1.left.right = Node(2)  # type: ignore

root2 = Node(1)
root2.left = Node(4)  # type: ignore
root2.left.left = Node(4)  # type: ignore
root2.left.right = Node(2)  # type: ignore


print(isIdentical(root1, root2))
