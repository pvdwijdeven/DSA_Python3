def sum_under_modulo(a, b) -> float | int:
	md = 10**9 + 7
	return (a % md + b % md) % md


if __name__ == "__main__":
	print(sum_under_modulo(a=9223372036854775807, b=9223372036854775807))
	print(sum_under_modulo(a=1000000007, b=1000000007))
