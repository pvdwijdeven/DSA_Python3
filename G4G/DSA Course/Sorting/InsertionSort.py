def insert(arr, index) -> list[int] | list[float]:
	for i in range(index - 1, -1, -1):
		if arr[i] > arr[index]:
			arr[index], arr[i] = arr[i], arr[index]
			index = i
		else:
			return arr
	return arr


# Function to sort the list using insertion sort algorithm.
def insertion_sort(arr, n) -> list[int] | list[float]:
	n = len(arr)
	for i in range(0, n):
		arr = insert(arr=arr, index=i)
	return arr


if __name__ == "__main__":
	arr = [4, 3, 5, 7, 2, 1, 6]
	n = len(arr)
	print(insertion_sort(arr=arr, n=n))
