from printTree import print_tree


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BST:

    # Function to print a node in a BST.
    def print_tree(self, node):
        print_tree(node)

    # Function to search a node in BST.
    def search(self, node, x):
        if node == None:
            return 0
        if node.data == x:
            return 1
        if node.data < x:
            return self.search(node.right, x)
        else:
            return self.search(node.left, x)

    # Function to insert a node in a BST.
    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.data == key:
                return root
            elif root.data < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def createBSTfromList(self, lst):
        root = None
        for key in lst:
            root = self.insert(root, key)
        return root

    def InOrder(self, root):
        arr = []
        if root != None:
            arr += self.InOrder(root.left)
            arr.append(root.data)
            arr += self.InOrder(root.right)
        return arr

    def deleteNode(self, root, X):
        # Find Closet greater value (in the right subtree)
        def get_successor(root):
            node = root.right
            while node and node.left:
                node = node.left
            return node

        if not root:
            return

        if X < root.data:
            root.left = self.deleteNode(root.left, X)
        elif X > root.data:
            root.right = self.deleteNode(root.right, X)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                succ = get_successor(root)
                root.data = succ.data
                root.right = self.deleteNode(root.right, succ.data)
        return root

    def preorder(self, root):
        arr = []
        if root != None:
            arr.append(root.data)
            arr += self.preorder(root.left)
            arr += self.preorder(root.right)
        return arr

    def inorder(self, root):
        arr = []
        if root != None:
            arr += self.inorder(root.left)
            arr.append(root.data)
            arr += self.inorder(root.right)
        return arr

    def postorder(self, root):
        arr = []
        if root != None:
            arr += self.postorder(root.left)
            arr += self.postorder(root.right)
            arr.append(root.data)
        return arr

    def levelOrder(self, root):
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

    def minValue(self, root):
        if root == None:
            return -1
        if root.left == None:
            return root.data
        else:
            return self.minValue(root.left)

    def maxValue(self, root):
        if root == None:
            return -1
        if root.right == None:
            return root.data
        else:
            return self.minValue(root.right)

    def floor(self, root, x):
        # code here
        if not root:
            return -1
        node = root
        res = -1
        while node:
            if node.data == x:
                return node.data
            if x < node.data:
                node = node.left
            else:
                res = node.data
                node = node.right
        return res

    def ceil(self, root, x):
        # code here
        if not root:
            return -1
        node = root
        res = None
        while node:
            if node.data == x:
                return node.data
            if x > node.data:
                node = node.right
            else:
                res = node.data
                node = node.left
        return res


my_bst = BST()
root = my_bst.createBSTfromList([71, 53, 11, 8, 13, 36, 10, 49, 14, 2])
my_bst.print_tree(root)
print(my_bst.minValue(root))
print(my_bst.floor(root, 12))
print(my_bst.ceil(root, 12))
