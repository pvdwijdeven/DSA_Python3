def find_triplets(arr, n) -> bool:
	n = len(arr)
	arr.sort()
	for i in range(0, n-1):
		l = i + 1
		r = n - 1
		x = arr[i]
		while (l < r):
			if (x + arr[l] + arr[r] == 0):
				return True
			elif (x + arr[l] + arr[r] < 0):
				l += 1
			else:
				r -= 1            
	return False

if __name__ == "__main__":
	arr = [0, -1, 2, -3, 1]
	n = len(arr)
	find_triplets(arr=arr, n=n)