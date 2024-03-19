def bubble_sort(arr) -> list[int] | list[float]:
	n = len(arr)
	for i in range(n):
		swapped = False
		for j in range(n - i - 1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		if not swapped:
			return arr
	return arr


if __name__ == "__main__":
	arr = [4, 1, 3, 9, 7]
	print(bubble_sort(arr=arr))
	arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	print(bubble_sort(arr=arr))
