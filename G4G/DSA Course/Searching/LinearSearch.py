def linear_search(arr, X) -> int:
	left = 0
	length = len(arr)
	position = -1
	right = length - 1
	# Run loop from 0 to right
	for left in range(0, right, 1):
		# If search_element is found with
		# left variable
		if arr[left] == X:
			position = left
			return position
		# If search_element is found with# right variable
		if arr[right] == X:
			position = right
			return position
		left += 1
		right -= 1

	# If element not found
	return -1


if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5]
	X = 5

	print(linear_search(arr=arr, X=X))
