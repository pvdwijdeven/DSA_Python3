from math import floor, sqrt


def is_prime(N) -> bool:
	if N <= 1:
		return False
	elif N <= 3:
		return True
	elif N % 2 == 0 or N % 3 == 0:
		return False

	i = 5
	while i * i <= N:
		if N % i == 0 or N % (i + 2) == 0:
			return False
		i += 6

	return True


def exactly_X_divisors(N, X) -> bool:
	total = 0
	for x in range(2, floor(sqrt(N)) + 1):
		if is_prime(N=x):
			total += 1
	return total == X


if __name__ == "__main__":
	print(exactly_X_divisors(N=30, X=3))
	print(exactly_X_divisors(N=8, X=3))
