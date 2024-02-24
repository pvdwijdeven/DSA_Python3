from typing import Any


class Node:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right


class BST:

    def __init__(self, arr=None) -> None:
        # create empty root
        if not arr:
            self.root = Node(data=None)
        else:
            self.build_tree(lst=arr)

    def print_tree(self, val="data", left="left", right="right") -> None:
        # function to print tree in a grahical way
        def display(root, val=val, left=left, right=right) -> Any:
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
                lines, n, p, x = display(root=getattr(root, right))
                s = "%s" % getattr(root, val)
                u = len(s)
                first_line = s + x * "_" + (n - x) * " "
                second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
                shifted_lines = [u * " " + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(root=getattr(root, left))
            right, m, q, y = display(root=getattr(root, right))
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

        lines, *_ = display(root=self.root, val=val, left=left, right=right)
        for line in lines:
            print(line)

    # Function to search a node in BST.
    def search(self, root, value) -> bool:
        if root == None:
            return False
        if root.data == value:
            return True
        if root.data < value:
            return self.search(root=root.right, value=value)
        else:
            return self.search(root=root.left, value=value)

    # Function to insert a node in a BST.
    def insert(self, data) -> Any | Node:
        parent = None
        root = self.root
        curr = root
        while curr:
            parent = curr
            if curr.data == data:
                return root
            elif curr.data < data:
                curr = curr.right
            else:
                curr = curr.left
        if not parent:
            return Node(data=data)
        assert parent
        if parent.data > data:
            parent.left = Node(data=data)
        else:
            parent.right = Node(data=data)
        return root

    def build_tree(self, lst) -> Node | None:
        self.root = None
        for key in lst:
            self.root = self.insert(data=key)
        return self.root

    def InOrder(self, root) -> list[Any]:
        arr = []
        if root:
            arr += self.InOrder(root=root.left)
            arr.append(root.data)
            arr += self.InOrder(root=root.right)
        return arr

    def deleteNode(self, value) -> Node | None:
        root = self.root
        parent = None
        current = root

        # Search for the node to delete
        while current and current.data != value:
            parent = current
            if current.data > value:
                current = current.left
            else:
                current = current.right

        # If node not found, return
        if current is None:
            return root

        # Case 1: Node to be deleted has no children or only one child
        if current.left is None:
            if parent is None:
                root = current.right
            elif parent.left == current:
                parent.left = current.right
            else:
                parent.right = current.right

        elif current.right is None:
            if parent is None:
                root = current.left
            elif parent.left == current:
                parent.left = current.left
            else:
                parent.right = current.left

        # Case 2: Node to be deleted has two children
        else:
            succ_parent = current
            succ = current.right

            while succ.left is not None:
                succ_parent = succ
                succ = succ.left

            if succ_parent != current:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right

            current.data = succ.data
        self.root = root
        return root

    def preorder(self, root) -> list[Any]:
        arr = []
        if root:
            arr.append(root.data)
            arr += self.preorder(root=root.left)
            arr += self.preorder(root=root.right)
        return arr

    def inorder(self, root) -> list[Any]:
        arr = []
        if root != None:
            arr += self.inorder(root=root.left)
            arr.append(root.data)
            arr += self.inorder(root=root.right)
        return arr

    def postorder(self) -> list[Any]:
        def get_postorder(root) -> list[Any]:
            arr = []
            if root != None:
                arr += get_postorder(root=root.left)
                arr += get_postorder(root=root.right)
                arr.append(root.data)
            return arr

        return get_postorder(root=self.root)

    def levelOrder(self) -> list[Any]:
        root = self.root
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

    def min_value(self) -> Any:
        if self.root is None:
            return -1
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def max_value(self) -> Any:
        if self.root is None:
            return -1
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

    def floor(self, value) -> Any:
        root = self.root
        if not root:
            return -1
        node = root
        res = -1
        while node:
            if node.data == value:
                return node.data
            if value < node.data:
                node = node.left
            else:
                res = node.data
                node = node.right
        return res

    def ceil(self, value) -> Any:
        root = self.root
        if not root:
            return -1
        node = root
        res = None
        while node:
            if node.data == value:
                return node.data
            if value > node.data:
                node = node.right
            else:
                res = node.data
                node = node.left
        return res


bst1 = BST(arr=[71, 53, 11, 8, 13, 36, 10, 49, 1, 2])
bst1.print_tree()

bst1.deleteNode(value=71)
bst1.print_tree()

print(bst1.min_value())
bst1.deleteNode(value=53)
print(bst1.max_value())


print(bst1.floor(value=12))
print(bst1.ceil(value=12))
