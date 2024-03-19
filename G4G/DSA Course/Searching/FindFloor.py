def find_floor(A, N, X) -> int:
	low = 0
	high = len(A) - 1

	while low <= high:
		mid = low + (high - low) // 2
		if (
			(A[mid] <= X and mid == N - 1)
			or A[mid] == X
			or (A[mid] < X and A[mid + 1] > X)
		):
			return mid
		elif A[mid] < X:
			low = mid + 1
		else:
			high = mid - 1
	return -1


if __name__ == "__main__":
	A = [1, 2, 8, 10, 11, 12, 19]
	N = len(A)
	X = 0
	print(find_floor(A=A, N=N, X=X))

	A = [1, 2, 8, 10, 11, 12, 19]
	N = len(A)
	X = 5
	print(find_floor(A=A, N=N, X=X))
