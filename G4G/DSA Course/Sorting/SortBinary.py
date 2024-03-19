def sort_binary(arr) -> list[int]:
	N = len(arr)
	left, right = 0, N - 1
	while left < right:
		while left < right and arr[left] == 0:
			left += 1
		while left < right and arr[right] == 1:
			right -= 1
		if left < right:
			arr[left], arr[right] = arr[right], arr[left]
			left += 1
			right -= 1
	return arr


if __name__ == "__main__":
	print(sort_binary(arr=[0, 1, 1, 1, 0, 0]))
