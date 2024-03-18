class Node:
    def __init__(self, val) -> None:
      self.data: int | float = val
      self.left: Node | None = None
      self.right: Node | None = None
    

# Function to return a list containing the preorder traversal of the tree.
def isIdentical(root1, root2):
    # code here
    res = True

    if root1 and root2:
        if root1.data != root2.data:
            return False
        res = isIdentical(root1.left, root2.left)
        res = res and isIdentical(root1.right, root2.right)
    else:
        if root1 != root2:
            return False
    return res

if __name__ == "__main__":
    root1 = Node(1)
    root1.left = Node(4)  # type: ignore
    root1.left.left = Node(4)  # type: ignore
    root1.left.right = Node(2)  # type: ignore
    
    root2 = Node(1)
    root2.left = Node(4)  # type: ignore
    root2.left.left = Node(4)  # type: ignore
    root2.left.right = Node(2)  # type: ignore
    
    
    print(isIdentical(root1, root2))
    