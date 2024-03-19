def factorial(N) -> int:
	if N == 0:
		return 1
	ans = N
	if N != 1:
		ans *= factorial(N=N - 1)
	return ans


if __name__ == "__main__":
	print(factorial(N=100))
