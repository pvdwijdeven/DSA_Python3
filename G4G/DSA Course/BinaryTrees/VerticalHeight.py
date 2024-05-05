# Program to print binary tree in vertical order


# A binary tree
class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.left: Node | None = None
        self.right: Node | None = None


# A utility function to find min and max distances with
# respect to root
def find_min_max(node, minimum, maximum, hd):

    # Base Case
    if node is None:
        return

    # Update min and max
    if hd < minimum[0]:
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd

    # Recur for left and right subtrees
    find_min_max(node.left, minimum, maximum, hd - 1)
    find_min_max(node.right, minimum, maximum, hd + 1)


# A utility function to print all nodes on a given line_no
# hd is horizontal distance of current node with respect to root
def get_vertical_line(node, line_no, hd, res):

    # Base Case
    if node is None:
        return res

    # If this node is on the given line number
    if hd == line_no:
        res.append(node.data)

    # Recur for left and right subtrees
    res = get_vertical_line(node.left, line_no, hd - 1, res)
    res = get_vertical_line(node.right, line_no, hd + 1, res)
    return res


def vertical_order(root):

    # Find min and max distances with respect to root
    minimum = [0]
    maximum = [0]
    find_min_max(root, minimum, maximum, 0)
    res = []
    # Iterate through all possible lines starting
    # from the leftmost line and print nodes line by line
    for line_no in range(minimum[0], maximum[0] + 1):
        res.append(get_vertical_line(root, line_no, 0, []))
    return res


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

print("Vertical order traversal is")
res = vertical_order(root)
print(res)
print(len(res))
