def longest_conseq_subarray(arr):
	hash = set()
	n = len(arr)
	res = 0
	for element in arr:
		hash.add(element)
	for i in range(n):
		if (arr[i] - 1) not in hash:
			j = arr[i]
			while j in hash:
				j += 1
			res = max(res, j - arr[i])
	return res


if __name__ == "__main__":
	arr = [12, 1, 9, 3, 10, 4, 20, 2, 11, 13]
	print(longest_conseq_subarray(arr=arr))
