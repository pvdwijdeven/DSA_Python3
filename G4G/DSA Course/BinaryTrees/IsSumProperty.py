# Function to check whether all nodes of a tree have the value
# equal to the sum of their child nodes.
def is_sum_property(node) -> int:
    def post_order(root) -> bool:
        res = True
        if root:
            res = res and post_order(root=root.left)
            res = res and post_order(root=root.right)
            lval = 0 if not root.left else root.left.data
            rval = 0 if not root.right else root.right.data
            return res and (
                (root.data == (lval + rval)) or (not root.left and not root.right)
            )
        return res

    return 1 if post_order(root=node) else 0
