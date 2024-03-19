def count_vowels_distinct(s) -> int:
	total = 0
	vowels = "aeoiu"
	for char in vowels:
		if char in s:
			total += 1
	return total


def count_vowels(s) -> int:
	total = 0
	vowels = "aeoiu"
	for char in s:
		if char in vowels:
			total += 1
	return total


if __name__ == "__main__":
	s = "hyena"
	print(count_vowels(s=s))
	s = "appeltaart"
	print(count_vowels(s=s))
	print(count_vowels_distinct(s=s))
