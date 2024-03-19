def sum_of_digits(n)-> int:
	if n == 0:
		return 0
	return (n % 10 + sum_of_digits(n=n // 10))

if __name__ == "__main__":
	print(sum_of_digits(n=1234))