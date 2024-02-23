from typing import Any


class Node:
    def __init__(self, val) -> None:
        self.data = val
        self.left = None
        self.right = None


class BT:
    def __init__(self, arr=None) -> None:
        # create empty root
        if not arr:
            self.root = Node(val=None)
        else:
            self.build_tree(lst=arr)

    def get_root(self) -> Node | None:
        # function to retrieve root for external programs
        return self.root

    def build_tree(self, lst) -> Node | None:
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
        self.root = grab(it=it, next_level=next_level)

        while next_level:
            level = next_level
            next_level = []
            for node in level:
                node.left = grab(it=it, next_level=next_level)
                node.right = grab(it=it, next_level=next_level)

        return self.root

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

    def is_balanced(self) -> bool:
        # function to check if tree is balanced
        def height(root) -> int:
            if not root:
                return 0
            leftheight, rightheight = height(root=root.left), height(root=root.right)
            if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:
                return -1
            return max(leftheight, rightheight) + 1

        return height(root=self.root) >= 0

    def is_sum_property(self) -> bool:
        # check if parent is always sum of children
        def scan_tree(root) -> bool:
            res = True
            if root:
                res = res and scan_tree(root=root.left)
                res = res and scan_tree(root=root.right)
                lval = 0 if not root.left else root.left.data
                rval = 0 if not root.right else root.right.data
                return res and (
                    (root.data == (lval + rval)) or (not root.left and not root.right)
                )
            return res

        return scan_tree(root=self.root)

    def get_height(self) -> int:
        # return height of tree
        def height(root) -> int:
            return (
                0
                if not root
                else max(height(root=root.left) + 1, height(root=root.right) + 1)
            )

        return height(root=self.root)

    def get_pre_order(self) -> list[Any]:
        # get pre-order traversal array of tree
        def pre_order(root) -> list[Any]:
            arr = []
            if root:
                arr.append(root.data)
                arr += pre_order(root=root.left)
                arr += pre_order(root=root.right)
            return arr

        return pre_order(root=self.root)

    def get_in_order(self) -> list[Any]:
        # get in-order traversal array of tree
        def in_order(root) -> list[Any]:
            arr = []
            if root:
                arr += in_order(root=root.left)
                arr.append(root.data)
                arr += in_order(root=root.right)
            return arr

        return in_order(root=self.root)

    def get_post_order(self) -> list[Any]:
        # get post-order traversal array of tree
        def post_order(root) -> list[Any]:
            arr = []
            if root:
                arr += post_order(root=root.left)
                arr += post_order(root=root.right)
                arr.append(root.data)
            return arr

        return post_order(root=self.root)

    def get_level_order(self) -> list[Any]:
        # get level-order traversal array of tree
        def level_order(root) -> list[Any]:
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

        return level_order(root=self.root)

    @classmethod
    def compare_tree(cls, root1, root2) -> bool:
        def is_identical(root1, root2) -> bool:

            res = True

            if root1 and root2:
                if root1.data != root2.data:
                    return False
                res = is_identical(root1=root1.left, root2=root2.left)
                res = res and is_identical(root1=root1.right, root2=root2.right)
            else:
                if root1 != root2:
                    return False
            return res

        return is_identical(root1=root1.root, root2=root2.root)


if __name__ == "__main__":
    bt = BT(arr=[3, 2, 1, 4, 5])
    bt.print_tree()
    print(bt.is_balanced())
    print(bt.is_sum_property())
    print(bt.get_height())
    print(bt.get_pre_order())
    print(bt.get_in_order())
    print(bt.get_post_order())
    print(bt.get_level_order())

    bt2 = BT(arr=[3, 2, 1, 4, 5])
    bt3 = BT(arr=[3, "N", 1, 4, 5])
    bt3.print_tree()
    print(BT.compare_tree(root1=bt, root2=bt2))
    print(BT.compare_tree(root1=bt, root2=bt3))
