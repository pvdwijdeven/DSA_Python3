def GCD(a, b) -> int:
	if b != 0:
		return GCD(a=b, b=a % b)
	else:
		return a


if __name__ == "__main__":
	print(GCD(a=15, b=5))
