mp = {}
preIndex = 0


class Node:
    def __init__(self, data):
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None


# Function to return a tree created from postorder and inoreder traversals.
class Solution:
    def buildTree(self, In, post, n):

        pIndex = [n - 1]
        return buildUtil(In, post, 0, n - 1, pIndex)


def buildUtil(In, post, inStrt, inEnd, pIndex):

    # Base case
    if inStrt > inEnd:
        return None

    # Pick current node from Postorder traversal
    # using postIndex and decrement postIndex
    node = Node(post[pIndex[0]])
    pIndex[0] -= 1

    # If this node has no children
    # then return
    if inStrt == inEnd:
        return node

    # Else find the index of this node
    # in Inorder traversal
    iIndex = search(In, inStrt, inEnd, node.data)

    # Using index in Inorder traversal,
    # construct left and right subtress
    assert node is not None
    node.right = buildUtil(In, post, iIndex + 1, inEnd, pIndex)
    node.left = buildUtil(In, post, inStrt, iIndex - 1, pIndex)

    return node


def search(arr, strt, end, value):
    i = 0
    for i in range(strt, end + 1):
        if arr[i] == value:
            break
    return i
