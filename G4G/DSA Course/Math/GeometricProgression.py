def termOfGP(a, r, N) -> int:
	return a * (int)(r ** (N - 1))

if __name__ == "__main__":
	print(termOfGP(a=2, r=3, N=1))
	print(termOfGP(a=1, r=2, N=5))
	print(termOfGP(a=2, r=3, N=5))
