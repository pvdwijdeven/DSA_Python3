# Function to check whether all nodes of a tree have the value
# equal to the sum of their child nodes.
def is_sum_property(node):
  # code here
  def post_order(root):
    # code here
    res = True
    if root:
      res = res and post_order(root.left)
      # print(root.data, res)
      res = res and post_order(root.right)
      # print(root.data, res)
      lval = 0 if not root.left else root.left.data
      rval = 0 if not root.right else root.right.data
      # print(root.data, lval, rval, root.data == (lval + rval))
      return res and ((root.data == (lval + rval)) or
                      (not root.left and not root.right))
    return res

  return 1 if post_order(node) else 0
