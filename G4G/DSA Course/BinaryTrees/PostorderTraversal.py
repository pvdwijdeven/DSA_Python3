class Node:
    def __init__(self, val) -> None:
      self.data: int | float = val
      self.left: Node | None = None
      self.right: Node | None = None
    

# Function to return a list containing the preorder traversal of the tree.
def postOrder(root):
    # code here
    arr = []
    if root:
        arr += postOrder(root.left)
        arr += postOrder(root.right)
        arr.append(root.data)
    return arr

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(4)  # type: ignore
    root.left.left = Node(4)  # type: ignore
    root.left.right = Node(2)  # type: ignore
    
    print(postOrder(root))
    