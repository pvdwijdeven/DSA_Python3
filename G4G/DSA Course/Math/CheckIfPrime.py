from math import floor, sqrt


def is_prime(N) -> bool:
	if N == 1:
		return False
	if N <= 3:
		return True
	if N % 2 == 0 or N % 3 == 0:
		return False
	top = floor(sqrt(N))
	return all(not (N % i == 0 or N % (i + 2) == 0) for i in range(5, top + 1, 6))


if __name__ == "__main__":
	print(is_prime(N=13))
	print(is_prime(N=131))
	print(is_prime(N=4))
	print(is_prime(N=5))
