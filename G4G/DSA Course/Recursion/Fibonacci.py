def fibonacci(n) -> int:
	if n == 1:
		return 1
	if n == 2:
		return 1
	return fibonacci(n=n - 1) + fibonacci(n=n - 2)


if __name__ == "__main__":
	print(fibonacci(n=20))
