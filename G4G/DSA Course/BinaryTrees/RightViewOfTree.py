class Solution:
	#Function to return list containing elements of right view of binary tree.
	def rightView(self, root):
		if root is None:
			return []

		ans = []
		q = [root]

		while len(q) != 0:
			count = len(q)
			for i in range(count):
				curr = q[0]
				q.pop(0)
				if i == count - 1:
					ans.append(curr.data)

				if curr.left is not None:
					q.append(curr.left)
				if curr.right is not None:
					q.append(curr.right)

		return ans
