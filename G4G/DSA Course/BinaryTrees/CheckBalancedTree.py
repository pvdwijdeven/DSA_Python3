class Node:

    def __init__(self, val) -> None:
        self.data: int | float = val
        self.left: Node | None = None
        self.right: Node | None = None


def isBalanced(root) -> bool:

    def Height(root) -> int:
        if not root:
            return 0
        leftheight, rightheight = Height(root=root.left), Height(root=root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1

    return Height(root=root) >= 0


if __name__ == "__main__":
    root = Node(val=1)
    temp = Node(val=4)
    root.left = Node(val=4)
    root.left.left = Node(val=4)
    root.left.right = Node(val=2)
    print(isBalanced(root=root))
