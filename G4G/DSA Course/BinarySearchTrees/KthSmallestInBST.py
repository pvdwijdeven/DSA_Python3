class Node:
    def __init__(self, k):
        self.left: None | Node = None
        self.right: None | Node = None
        self.key = k
        self.size = 1  # Initialize size to 1


def update_size(node):
    if node is not None:
        node.size = (
            1
            + (node.left.size if node.left else 0)
            + (node.right.size if node.right else 0)
        )


def printkth(root, k):
    if root is None:
        return None

    left_size = root.left.size if root.left else 0

    if k == left_size + 1:
        print(root.key)
        return

    elif k <= left_size:
        printkth(root.left, k)

    else:
        printkth(root.right, k - left_size - 1)


# Example usage:
root = Node(17)
root.left = Node(5)
root.left.left = Node(3)
root.right = Node(20)
root.right.left = Node(18)
root.right.left.left = Node(16)
root.right.right = Node(80)

k = 3
print("kth smallest:", end=" ")
printkth(root, k)
