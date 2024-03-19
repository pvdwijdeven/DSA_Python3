def is_panagram(s) -> bool:
	h = [0 for x in range(26)]
	for char in s:
		char = char.lower()
		if char.isalnum():
			h[ord(char) - 97] += 1
	return all(count != 0 for count in h)


if __name__ == "__main__":
	s1 = "The quick brown fox jumps over the lazy dog"
	s2 = "The quick brown fop jumps over the lazy dog"
	print(is_panagram(s=s1))
	print(is_panagram(s=s2))
