class Solution:
	#Function to convert a binary tree into its mirror tree.
	def mirror(self, root):
		if root == None:
			return
		root.left, root.right = self.mirror(root.right), self.mirror(root.left)
		return root
