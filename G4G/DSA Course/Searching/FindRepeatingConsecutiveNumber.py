def find_repeating_consecutive(arr) -> list[int]:

	# if array has no repeating element, we return (-1,-1).
	if len(arr) - (arr[len(arr) - 1] - arr[0]) == 1:
		return [-1, -1]
	left = 0
	right = len(arr) - 1
	# using binary search to find the repeating element.
	while left < right:
		mid = (left + right) // 2
		# if arr[mid]=mid+a[0], there is no repeating
		# number in [left..mid].
		if arr[mid] >= mid + arr[0]:
			left = mid + 1
		# else there is repeating number in [left..mid].
		else:
			right = mid
	# returning the repeated element and its frequency.
	return [arr[left], len(arr) - (arr[len(arr) - 1] - arr[0])]


if __name__ == "__main__":
	arr = [1, 2, 3, 3, 4, 5]
	print(find_repeating_consecutive(arr=arr))
	arr = [2, 3, 4, 5, 5, 5, 6, 7]
	print(find_repeating_consecutive(arr=arr))
	arr = [1, 2, 3]
	print(find_repeating_consecutive(arr=arr))
