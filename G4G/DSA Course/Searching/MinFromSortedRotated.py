# Function to find the minimum element in sorted and rotated array.
def minNumber(arr) -> int:
	n = len(arr)
	low = 0
	high = n - 1
	if arr[low] <= arr[high]:
		return arr[low]
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] < arr[mid - 1]:
			return arr[mid]
		if arr[high] < arr[mid]:
			low = mid + 1
		else:
			high = mid - 1
	return -1


if __name__ == "__main__":
	arr = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
	print(minNumber(arr=arr))
	arr = [3, 4, 5, 1, 2]
	print(minNumber(arr=arr))
	arr = [1, 2, 3, 4, 5]
	print(minNumber(arr=arr))
	arr = [5, 1, 2, 3, 4]
	print(minNumber(arr=arr))