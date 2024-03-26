# Function to return a list containing the intersection of two arrays.
def intersection_of_sorted_arrays(arr1, arr2) -> list[int]:
	res = []
	n = len(arr1)
	m = len(arr2)
	i = 0
	j = 0
	cur = float("inf")
	while i < n and j < m:
		if arr1[i] == arr2[j]:
			if cur != arr1[i]:
				cur = arr1[i]
				res.append(cur)
			i += 1
			j += 1
		elif arr1[i] > arr2[j]:
			j += 1
		else:
			i += 1
	if res == []:
		return [-1]
	return res


if __name__ == "__main__":
	a = [1, 2, 3, 4]
	b = [2, 2, 4, 6, 7, 8]
	print(intersection_of_sorted_arrays(arr1=a, arr2=b))
	a = [1, 2, 3, 4]
	b = [6, 7, 8]
	print(intersection_of_sorted_arrays(arr1=a, arr2=b))
