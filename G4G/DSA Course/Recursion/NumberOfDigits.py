def count_digits(n)->int:

	if n == 0:
		return 0
	return (1 + count_digits(n=n // 10))

if __name__ == "__main__":
	print(count_digits(n=1234))