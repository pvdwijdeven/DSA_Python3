# Python program to find the maximum width of binary
# tree using Level Order Traversal with queue.

from collections import deque


# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


# Function to get the maximum width of a binary tree


def getMaxWidth(root) -> int:
    if root is None:
        return 0

    maxWidth = 0
    level_size = 1
    q = deque([root])

    while q:
        maxWidth: int = max(maxWidth, level_size)
        level_size = 0
        next_level_size = 0

        for _ in range(len(q)):
            node = q.popleft()
            level_size += 1

            if node.left:
                q.append(node.left)
                next_level_size += 1

            if node.right:
                q.append(node.right)
                next_level_size += 1

        level_size: int = next_level_size

    return maxWidth


# Driver program to test above function
def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    # Function call
    print("Maximum width is %d" % (getMaxWidth(root)))


if __name__ == "__main__":
    main()
