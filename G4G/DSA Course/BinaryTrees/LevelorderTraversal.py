class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


# Function to return a list containing the preorder traversal of the tree.
def levelOrder(root):
    # code here
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


root = Node(1)
root.left = Node(4)  # type: ignore
root.left.left = Node(4)  # type: ignore
root.left.right = Node(2)  # type: ignore

print(levelOrder(root))
