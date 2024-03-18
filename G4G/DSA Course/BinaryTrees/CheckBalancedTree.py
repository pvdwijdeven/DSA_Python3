class Node:

    def __init__(self, val) -> None:
        self.data: int | float = val
        self.left: Node | None = None
        self.right: Node | None = None


def is_balanced(root) -> bool:

    def height(root) -> int:
        if not root:
            return 0
        height_left, height_right = height(root=root.left), height(root=root.right)
        if height_left < 0 or height_right < 0 or abs(height_left - height_right) > 1:
            return -1
        return max(height_left, height_right) + 1

    return height(root=root) >= 0


if __name__ == "__main__":
    root = Node(val=1)
    temp = Node(val=4)
    root.left = Node(val=4)
    root.left.left = Node(val=4)
    root.left.right = Node(val=2)
    print(is_balanced(root=root))
