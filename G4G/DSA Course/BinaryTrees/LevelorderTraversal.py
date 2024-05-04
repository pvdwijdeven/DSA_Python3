class Node:
    def __init__(self, val) -> None:
        self.data: int | float = val
        self.left: Node | None = None
        self.right: Node | None = None


# Function to return a list containing the level order traversal of the tree.
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


from collections import deque


def level_order_traversal2(root):
    res = []
    if root is None:
        return
    q = deque()
    q.append(root)
    q.append(None)
    while len(q) > 1:
        curr = q.popleft()
        if curr == None:
            q.append(None)
            continue
        res.append(curr.data)
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)
    return res


if __name__ == "__main__":
    root = Node(val=1)
    root.left = Node(val=4)
    root.left.left = Node(val=4)
    root.left.right = Node(val=2)

    print(level_order_traversal(root=root))
    print(level_order_traversal2(root=root))
