def missing_panagram(s) -> list[str]:
	res = []
	h = [0 for x in range(26)]
	for char in s:
		char = char.lower()
		if char.isalnum():
			h[ord(char) - 97] += 1
	for count in range(26):
		if h[count] == 0:
			res.append(chr(count + 97))
	return res


if __name__ == "__main__":
	s1 = "The quick brown fox jumps over the lazy dog"
	s2 = "The quick brown fop jumps over the lazy dog"
	print(missing_panagram(s=s1))
	print(missing_panagram(s=s2))
