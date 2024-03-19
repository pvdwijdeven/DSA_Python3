from math import floor, log


def digits_in_factorial(N) -> int:
	if N < 0:
		return 0
	if N <= 1:
		return 1
	digits = 0
	for x in range(2, N + 1):
		digits += log(x=x, base=10)
	return floor(digits) + 1


print(digits_in_factorial(N=10**9))
