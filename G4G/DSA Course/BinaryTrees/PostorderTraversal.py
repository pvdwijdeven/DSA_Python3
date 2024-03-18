class Node:
    def __init__(self, val) -> None:
        self.data: int | float = val
        self.left: Node | None = None
        self.right: Node | None = None


# Function to return a list containing the preorder traversal of the tree.
def pos_order_traversal(root) -> list[int]:
    arr = []
    if root:
        arr += pos_order_traversal(root=root.left)
        arr += pos_order_traversal(root=root.right)
        arr.append(root.data)
    return arr


if __name__ == "__main__":
    root = Node(val=1)
    root.left = Node(val=4)
    root.left.left = Node(val=4)
    root.left.right = Node(val=2)

    print(pos_order_traversal(root=root))
