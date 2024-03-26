# function to count all possible triangles within array
def number_of_triangles(arr) -> int:
	n = len(arr)
	arr.sort()
	count = 0
	for i in range(0, n - 2):
		k = i + 2
		for j in range(i + 1, n):
			while k < n and arr[i] + arr[j] > arr[k]:
				k += 1
			if k > j:
				count += k - j - 1
	return count


if __name__ == "__main__":
	arr = [10, 21, 22, 100, 101, 200, 300]
	print(number_of_triangles(arr=arr))
