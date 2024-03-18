class Node:
    def __init__(self, val) -> None:
        self.data: int | float = val
        self.left: Node | None = None
        self.right: Node | None = None


# Function to return a list containing the preorder traversal of the tree.
def level_order_traversal(root) -> list[int]:
    if not root:
        return []
    arr = []
    queue = []
    queue.append(root)
    while queue != []:
        node = queue.pop(0)
        arr.append(node.data)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
    return arr


if __name__ == "__main__":
    root = Node(val=1)
    root.left = Node(val=4)
    root.left.left = Node(val=4)
    root.left.right = Node(val=2)

    print(level_order_traversal(root=root))
