# Python program for conversion of
# binary tree to doubly linked list.
class Node:
    def __init__(self, val):
        self.right: Node | None = None
        self.data = val
        self.left: Node | None = None


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


# Global variable used in convert
prev = None

v = []


# Function to perform In-Order traversal of the
# tree and store the nodes in a vector
def inorder(root):
    global v

    if root == None:
        return

    # first recur on left child
    inorder(root.left)

    # append the data of node in vector
    v.append(root.data)

    # now recur on right child
    inorder(root.right)


# Function to convert Binary Tree to Circular
# Doubly Linked list using the vector which stores
# In-Order traversal of the Binary Tree
def bTreeToCList(root):

    global v

    # Base cases
    if root == None:
        return None

    # Vector to be used for storing the nodes
    # of tree in In-order form
    v = []

    # Calling the In-Order traversal function
    inorder(root)

    # Create the head of the linked list pointing
    # to the root of the tree
    head_ref = Node(v[0])

    # Create a current pointer to be used in traversal
    curr = head_ref

    i = 1

    # Traversing the nodes of the tree starting
    # from the second elements
    while i < len(v):

        # Create a temporary pointer
        # pointing to current
        temp = curr

        # Current's right points to the current
        # node in traversal
        curr.right = Node(v[i])

        # Current points to its right
        curr = curr.right

        # Current's left points to temp
        curr.left = temp
        i = i + 1

    # Current's right points to head of the list
    curr.right = head_ref

    # Head's left points to current
    head_ref.left = curr

    # Return head of the list
    return head_ref


def build_tree(lst) -> Node | None:
    # funtion to build tree from an array, where "N" represents empty node
    def grab(it, next_level) -> Node | None:
        value = next(it, "N")
        if value != "N":
            node = Node(val=value)
            next_level.append(node)
            return node

    # Create the root of the tree
    it = iter(lst)
    next_level = []
    root = grab(it=it, next_level=next_level)

    while next_level:
        level = next_level
        next_level = []
        for node in level:
            node.left = grab(it=it, next_level=next_level)
            node.right = grab(it=it, next_level=next_level)

    return root


def print_dll(head: Node | None):

    # Function to print nodes in given
    # doubly linked list
    cur: Node | None = head
    assert cur
    assert head
    print(cur.data, end=" ")
    cur = head.right
    while cur is not head:
        assert cur
        print(cur.data, end=" ")
        cur = cur.right
    print()
    assert cur
    cur = cur.left
    while cur != head:
        assert cur
        print(cur.data, end=" ")
        cur = cur.left
    print(head.data, end=" ")


# Driver program to test above functions
# Let us create the tree as
# shown in above diagram
if __name__ == "__main__":
    # root = Node(10)
    # root.left = Node(12)
    # root.right = Node(15)
    # root.left.left = Node(25)
    # root.left.right = Node(30)
    # root.right.left = Node(36)

    # head = BinaryTree2DoubleLinkedList(root)

    # print_dll(head)

    print("\nnext")

    arr = [10, 20, 30, 40, 60]
    root = build_tree(arr)

    print(level_order_traversal(root))

    head = bTreeToCList(root)

    # Print the converted list
    print_dll(head)
