class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def height(root):
    # code here
    return 0 if root is None else max(height(root.left) + 1, height(root.right) + 1)


root = Node(1)
root.left = Node(4)  # type: ignore
root.left.left = Node(4)  # type: ignore
root.left.right = Node(2)  # type: ignore

print(height(root))
