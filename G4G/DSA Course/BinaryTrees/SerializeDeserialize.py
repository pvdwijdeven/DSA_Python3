nodeVals = []
MARKER = -1


class Node:

	def __init__(self, val):
		self.val = val
		self.left: Node | None = None
		self.right: Node | None = None


def serialize(root):
	if root is None:
		nodeVals.append(MARKER)
		return

	nodeVals.append(root.val)
	serialize(root.left)
	serialize(root.right)


def deserialize(root, nodeVals):
	if nodeVals:
		val = nodeVals.pop(0)
	else:
		return

	if val == MARKER:
		return

	# Create root, left and right recursively
	root = Node(val)
	root.left = deserialize(root.left, nodeVals)
	root.right = deserialize(root.right, nodeVals)
	return root


def inorder_traversal(root):
	if root:
		inorder_traversal(root.left)
		print(root.val, end=" ")
		inorder_traversal(root.right)


if __name__ == "__main__":
	# Create tree
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.left.right.left = Node(6)
	root.left.right.right = Node(7)

	print("Inorder traversal before serialization is - ")
	inorder_traversal(root)
	print("")

	# serialize the tree and insert elements into a list
	serialize(root)
	print(nodeVals)

	root1 = None
	root1 = deserialize(root1, nodeVals)
	print("Inorder traversal after deserialization is - ")
	inorder_traversal(root1)
	print("")
