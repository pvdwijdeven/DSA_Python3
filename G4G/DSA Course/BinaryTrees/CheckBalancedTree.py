class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def isBalanced(root):
    def Height(root):
        if root is None:
            return 0
        leftheight, rightheight = Height(root.left), Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
            return -1
        return max(leftheight, rightheight) + 1

    return Height(root) >= 0


root = Node(1)

root.left = Node(4)  # type: ignore
root.left.left = Node(4)  # type: ignore
root.left.right = Node(2)  # type: ignore

print(isBalanced(root))
