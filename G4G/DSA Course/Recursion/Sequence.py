# S(n) = n+ n*(S(n-1)) and S(0) = 1
def the_sequence(n):
	if n == 0:
		return 1
	n = n + n * the_sequence(n - 1)
	return n


if __name__ == "__main__":
	print(the_sequence(2))
	print(the_sequence(3))
	print(the_sequence(10))
