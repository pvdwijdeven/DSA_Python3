class Node:
    def __init__(self, val) -> None:
        self.data: int | float = val
        self.left: Node | None = None
        self.right: Node | None = None


# Function to return a list containing the preorder traversal of the tree.
def is_identical(root1, root2) -> bool:
    res = True
    if root1 and root2:
        if root1.data != root2.data:
            return False
        res = is_identical(root1=root1.left, root2=root2.left)
        res = res and is_identical(root1=root1.right, root2=root2.right)
    else:
        if root1 != root2:
            return False
    return res


if __name__ == "__main__":
    root1 = Node(val=1)
    root1.left = Node(val=4)
    root1.left.left = Node(val=4)
    root1.left.right = Node(val=2)

    root2 = Node(val=1)
    root2.left = Node(val=4)
    root2.left.left = Node(val=4)
    root2.left.right = Node(val=2)

    print(is_identical(root1=root1, root2=root2))
