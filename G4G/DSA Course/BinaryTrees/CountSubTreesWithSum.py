def countSubtreesWithSumX(root, x):
	subtree_cnt = 0

	def find_cnt(root, x):
		nonlocal subtree_cnt
		if not root:
			return 0

		cur_sum = root.data + find_cnt(root.left, x) + find_cnt(root.right, x)

		if cur_sum == x:
			subtree_cnt += 1

		return cur_sum

	find_cnt(root, x)
	return subtree_cnt
