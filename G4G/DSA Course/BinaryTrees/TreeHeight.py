class Node:
    def __init__(self, val) -> None:
        self.data: int | float = val
        self.left: Node | None = None
        self.right: Node | None = None


def height(root) -> int:
    return (
        0
        if root is None
        else max(height(root=root.left) + 1, height(root=root.right) + 1)
    )


if __name__ == "__main__":
    root = Node(val=1)
    root.left = Node(val=4)
    root.left.left = Node(val=4)
    root.left.right = Node(val=2)

    print(height(root=root))
