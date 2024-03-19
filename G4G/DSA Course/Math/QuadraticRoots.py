from math import sqrt, floor


def quadratic_roots(a, b, c) -> list[int]:
	if b**2 - 4 * a * c < 0:
		return [-1]
	return sorted(
	    [
	        floor((-1 * b + (sqrt(b**2 - 4 * a * c))) / (2 * a)),
	        floor((-1 * b - (sqrt(b**2 - 4 * a * c))) / (2 * a)),
	    ],
	    reverse=True,
	)


if __name__ == "__main__":
	print(quadratic_roots(a=1, b=10, c=-24))
	print(quadratic_roots(a=11, b=12, c=13))
