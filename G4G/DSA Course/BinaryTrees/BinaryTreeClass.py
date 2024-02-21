class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BT:
    def __init__(self, arr=None):
        # create empty root
        if not arr:
            self.root = Node(None)
        else:
            self.buildTree(arr)

    def get_root(self):
        # function to retrieve root for external programs
        return self.root

    def buildTree(self, lst):
        # funtion to build tree from an array, where "N" represents empty node
        def grab(it, nextlevel):
            value = next(it, "N")
            if value != "N":
                node = Node(value)
                nextlevel.append(node)
                return node

        # Create the root of the tree
        it = iter(lst)
        nextlevel = []
        self.root = grab(it, nextlevel)

        while nextlevel:
            level = nextlevel
            nextlevel = []
            for node in level:
                node.left = grab(it, nextlevel)
                node.right = grab(it, nextlevel)

        return self.root

    def print_tree(self, val="data", left="left", right="right"):
        # function to print tree in a grahical way
        def display(root, val=val, left=left, right=right):
            # Returns list of strings, width, height, and horizontal coordinate of the root.
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = "%s" % getattr(root, val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = "%s" % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * " " + (n - x - 1) * "_" + s
                second_line = x * " " + "/" + (n - x - 1 + u) * " "
                shifted_lines = [line + u * " " for line in lines]
                return (
                    [first_line, second_line] + shifted_lines,
                    n + u,
                    p + 2,
                    n + u // 2,
                )

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = "%s" % getattr(root, val)
                u = len(s)
                first_line = s + x * "_" + (n - x) * " "
                second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
                shifted_lines = [u * " " + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = "%s" % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
            second_line = (
                x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
            )
            if p < q:
                left += [n * " "] * (q - p)
            elif q < p:
                right += [m * " "] * (p - q)
            zipped_lines = zip(left, right, strict=True)
            lines = [first_line, second_line] + [
                a + u * " " + b for a, b in zipped_lines
            ]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(self.root, val, left, right)
        for line in lines:
            print(line)

    def isBalanced(self):
        # function to check if tree is balanced
        def Height(root):
            if not root:
                return 0
            leftheight, rightheight = Height(root.left), Height(root.right)
            if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
                return -1
            return max(leftheight, rightheight) + 1

        return Height(self.root) >= 0

    def isSumProperty(self):
        # check if parent is always sum of children
        def scanTree(root):
            res = True
            if root:
                res = res and scanTree(root.left)
                res = res and scanTree(root.right)
                lval = 0 if not root.left else root.left.data
                rval = 0 if not root.right else root.right.data
                return res and (
                    (root.data == (lval + rval)) or (not root.left and not root.right)
                )
            return res

        return scanTree(self.root)

    def getHeight(self):
        # return height of tree
        def height(root):
            return 0 if not root else max(height(root.left) + 1, height(root.right) + 1)

        return height(self.root)

    def getPreOrder(self):
        # get pre-order traversal array of tree
        def preOrder(root):
            arr = []
            if root:
                arr.append(root.data)
                arr += preOrder(root.left)
                arr += preOrder(root.right)
            return arr

        return preOrder(self.root)

    def getInOrder(self):
        # get in-order traversal array of tree
        def inOrder(root):
            arr = []
            if root:
                arr += inOrder(root.left)
                arr.append(root.data)
                arr += inOrder(root.right)
            return arr

        return inOrder(self.root)

    def getPostOrder(self):
        # get post-order traversal array of tree
        def postOrder(root):
            arr = []
            if root:
                arr += postOrder(root.left)
                arr += postOrder(root.right)
                arr.append(root.data)
            return arr

        return postOrder(self.root)

    def getLevelOrder(self):
        # get level-order traversal array of tree
        def levelOrder(root):
            if not root:
                return []
            arr = []
            queue = []
            queue.append(root)
            while queue != []:
                node = queue.pop(0)
                arr.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            return arr

        return levelOrder(self.root)

    def compareTree(self, root2):
        def isIdentical(root1, root2):
            # code here
            res = True

            if root1 and root2:
                if root1.data != root2.data:
                    return False
                res = isIdentical(root1.left, root2.left)
                res = res and isIdentical(root1.right, root2.right)
            else:
                if root1 != root2:
                    return False
            return res

        return isIdentical(self.root, root2.root)


bt = BT([3, 2, 1, 4, 5])
bt.print_tree()
print(bt.isBalanced())
print(bt.isSumProperty())
print(bt.getHeight())
print(bt.getPreOrder())
print(bt.getInOrder())
print(bt.getPostOrder())
print(bt.getLevelOrder())

bt2 = BT([3, 2, 1, 4, 5])
bt3 = BT([3, "N", 1, 4, 5])
bt3.print_tree()
print(bt.compareTree(bt2))
print(bt.compareTree(bt3))
