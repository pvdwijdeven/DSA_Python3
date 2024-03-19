def left_index(arr, X) -> int:
	# code here
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = low + (high - low) // 2
		if arr[mid] == X and (mid == 0 or arr[mid - 1] != X):
			return mid
		elif arr[mid] < X:
			low = mid + 1
		else:
			high = mid - 1
	return -1


if __name__ == "__main__":
	arr = [1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
	X = 3

	print(left_index(arr=arr, X=X))
