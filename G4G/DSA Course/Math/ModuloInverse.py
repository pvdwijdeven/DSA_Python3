# Given two integers N and M, find the modular multiplicative inverse of A under modulo M.
# The modular multiplicative inverse is an integer X such that:
# A * X (mod M) = 1
def modulo_inverse(N, M) -> int:
	for x in range(1, M):
		if (x * N) % M == 1:
			return x
	return -1


if __name__ == "__main__":
	print(modulo_inverse(N=3, M=11))
	print(modulo_inverse(N=10, M=17))
	print(modulo_inverse(N=3, M=7))