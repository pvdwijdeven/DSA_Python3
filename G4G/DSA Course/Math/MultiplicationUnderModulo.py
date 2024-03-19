def multiplication_under_modulo(a, b) -> int:
	md = 10**9 + 7
	return (a % md * b % md) % md


if __name__ == "__main__":
	print(multiplication_under_modulo(a=92233720368547758,
	                                  b=92233720368547758))
	print(multiplication_under_modulo(a=1000000007, b=1000000007))
