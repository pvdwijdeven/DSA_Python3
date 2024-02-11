class Solution:
    # Function to check whether all nodes of a tree have the value
    # equal to the sum of their child nodes.
    def isSumProperty(self, node):
        # code here
        def postOrder(root):
            # code here
            res = True
            if root != None:
                res = res and postOrder(root.left)
                # print(root.data, res)
                res = res and postOrder(root.right)
                # print(root.data, res)
                lval = 0 if root.left == None else root.left.data
                rval = 0 if root.right == None else root.right.data
                # print(root.data, lval, rval, root.data == (lval + rval))
                return res and (
                    (root.data == (lval + rval))
                    or (root.left == None and root.right == None)
                )
            return res

        return 1 if postOrder(node) else 0
