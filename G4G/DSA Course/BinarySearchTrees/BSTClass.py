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
    def search(self, value) -> bool:
        def get_search(root, value) -> bool:
            if not root:
                return False
            if root.data == value:
                return True
            if root.data < value:
                return get_search(root=root.right, value=value)
            else:
                return get_search(root=root.left, value=value)

        return get_search(root=self.root, value=value)

    # Function to insert a node in a BST.
    def insert(self, data) -> Node:
        def get_insert(root, value) -> Node:
            if not root:
                return Node(data=value)
            else:
                if root.data == value:
                    return root
                elif root.data < value:
                    root.right = get_insert(root=root.right, value=value)
                else:
                    root.left = get_insert(root=root.left, value=value)
            return root

        return get_insert(root=self.root, value=data)

    def build_tree(self, lst) -> Node | None:
        self.root = None
        for value in lst:
            self.root = self.insert(data=value)
        return self.root

    def delete_node(self, value) -> Node | None:

        def get_suc(cur) -> Any:
            while cur.left:
                cur = cur.left
            return cur.data

        def get_delete_node(root, value) -> Node | None:
            if not root:
                return
            if root.data > value:
                root.left = get_delete_node(root=root.left, value=value)
            if root.data < value:
                root.right = get_delete_node(root=root.right, value=value)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    suc = get_suc(cur=root.right)
                    root.data = suc
                    root.right = get_delete_node(root=root.right, value=suc)
            return root

        self.root = get_delete_node(root=self.root, value=value)
        return self.root

    def preorder(self) -> list[Any]:
        def get_preorder(root) -> list[Any]:
            arr = []
            if root:
                arr.append(root.data)
                arr += get_preorder(root=root.left)
                arr += get_preorder(root=root.right)
            return arr

        return get_preorder(root=self.root)

    def inorder(self) -> list[Any]:
        def get_inorder(root) -> list[Any]:
            arr = []
            if root:
                arr += get_inorder(root=root.left)
                arr.append(root.data)
                arr += get_inorder(root=root.right)
            return arr

        return get_inorder(root=self.root)

    def postorder(self) -> list[Any]:
        def get_postorder(root) -> list[Any]:
            arr = []
            if root:
                arr += get_postorder(root=root.left)
                arr += get_postorder(root=root.right)
                arr.append(root.data)
            return arr

        return get_postorder(root=self.root)

    def levelorder(self) -> list[Any]:
        root = self.root
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

    def min_value(self) -> Any:
        if not self.root:
            return -1
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.data

    def max_value(self) -> Any:
        if not self.root:
            return -1
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.data

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


if __name__ == "__main__":
    bst1 = BST(arr=[71, 53, 11, 8, 13, 36, 10, 49, 1, 2])
    bst1.print_tree()

    bst1.delete_node(value=71)
    bst1.print_tree()

    print(bst1.min_value())
    bst1.delete_node(value=53)
    print(bst1.max_value())

    print(bst1.preorder())
    print(bst1.inorder())
    print(bst1.postorder())
    print(bst1.levelorder())

    print(bst1.search(value=49))
    print(bst1.search(value=53))

    print(bst1.floor(value=12))
    print(bst1.ceil(value=12))
