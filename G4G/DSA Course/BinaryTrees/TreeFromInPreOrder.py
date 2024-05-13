# Python3 program to construct tree using inorder
# and preorder traversals


# A binary tree node has data, pointer to left child
# and a pointer to right child
class Node:

    def __init__(self, x):

        self.data = x
        self.left: Node | None = None
        self.right: Node | None = None


mp = {}
preIndex = 0


# Recursive function to construct binary of size
# len from Inorder traversal in[] and Preorder traversal
# pre[]. Initial values of inStrt and inEnd should be
# 0 and len -1. The function doesn't do any error
# checking for cases where inorder and preorder
# do not form a tree
def buildTree(inn, pre, inStrt, inEnd):

    global preIndex, mp

    if inStrt > inEnd:
        return None

    # Pick current node from Preorder traversal
    # using preIndex and increment preIndex
    curr = pre[preIndex]
    preIndex += 1
    tNode = Node(curr)

    # If this node has no children then return
    if inStrt == inEnd:
        return tNode

    # Else find the index of this
    # node in Inorder traversal
    inIndex = mp[curr]

    # Using index in Inorder traversal,
    # construct left and right subtress
    tNode.left = buildTree(inn, pre, inStrt, inIndex - 1)
    tNode.right = buildTree(inn, pre, inIndex + 1, inEnd)

    return tNode


# This function mainly creates an
# unordered_map, then calls buildTree()
def buldTreeWrap(inn, pre, lenn):

    global mp

    # Store indexes of all items so that we
    # we can quickly find later
    # unordered_map<char, int> mp;
    for i in range(lenn):
        mp[inn[i]] = i

    return buildTree(inn, pre, 0, lenn - 1)


# This function is here just to test buildTree()
def printInorder(node):

    if node == None:
        return

    printInorder(node.left)
    print(node.data, end=" ")
    printInorder(node.right)


# Driver code
if __name__ == "__main__":

    inn = ["D", "B", "E", "A", "F", "C"]
    pre = ["A", "B", "D", "E", "C", "F"]
    lenn = len(inn)

    root = buldTreeWrap(inn, pre, lenn)

    # Let us test the built tree by printing
    # Inorder traversal
    print("Inorder traversal of " "the constructed tree is")

    printInorder(root)
