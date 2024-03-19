def lomuto_partition(arr, l, h):
	pivot = arr[h]
	i = l - 1
	for j in range(l, h):
		if arr[j] <= pivot:  # error
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[h] = arr[h], arr[i + 1]
	return i + 1


def hoarse_partition(arr, l, h):
	pivot = arr[l]
	i = l - 1
	j = h + 1
	while True:
		i = i + 1
		while arr[i] < pivot:
			i = i + 1
		j = j - 1
		while arr[j] > pivot:
			j = j - 1
		if i >= j:
			return j
		arr[i], arr[j] = arr[j], arr[i]


def qSort(arr, l=0, h=None, partition=lomuto_partition):
	if h == None:
		h = len(arr) - 1
	par = 0 if partition == hoarse_partition else 1
	if l < h:
		p = partition(arr, l, h)
		qSort(arr=arr, l=l, h=p - par, partition=partition)
		qSort(arr=arr, l=p + 1, h=h, partition=partition)


if __name__ == "__main__":
	arr = [8, 4, 7, 9, 3, 10, 5]
	qSort(arr=arr, partition=hoarse_partition)
	print(*arr)
	arr = [8, 4, 7, 9, 3, 10, 5]
	qSort(arr=arr, partition=lomuto_partition)
	print(*arr)
