def heapify(arr, n, i) -> None:
	largest = i  # Initialize largest as root
	l = 2 * i + 1  # left = 2*i + 1
	r = 2 * i + 2  # right = 2*i + 2
	if l < n and arr[i] < arr[l]:
		largest = l
	if r < n and arr[largest] < arr[r]:
		largest = r
	if largest != i:
		(arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
		heapify(arr=arr, n=n, i=largest)


def heapSort(arr) -> None:
	n = len(arr)
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr=arr, n=n, i=i)
	for i in range(n - 1, 0, -1):
		(arr[i], arr[0]) = (arr[0], arr[i])  # swap
		heapify(arr=arr, n=i, i=0)


if __name__ == "__main__":
	arr = [
	    12,
	    11,
	    13,
	    5,
	    6,
	    7,
	]
	heapSort(arr=arr)
	print('Sorted array is', arr)
