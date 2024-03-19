def palindrome(X) -> bool:
	X = str(X)
	if len(X) <= 1:
		return True
	if X[0] == X[-1]:
		return palindrome(X=X[1:-1])
	else:
		return False


if __name__ == "__main__":
	print(palindrome(X="parteretrap"))
	print(palindrome(X=1234321))
