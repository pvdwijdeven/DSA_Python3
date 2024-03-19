def correct_parenthesis(s) -> bool:
	stack = []
	opening = ["{", "(", "["]
	closing = ["}", ")", "]"]
	par = dict(map(lambda i, j: (i, j), closing, opening))
	for char in s:
		if char in opening:
			stack.append(char)
		if char in closing:
			if par[char] != stack.pop():
				return False
	return stack == []


if __name__ == "__main__":
	x = "{[()]}"
	print(correct_parenthesis(s=x))
	x = "{[]()}"
	print(correct_parenthesis(s=x))
	x = "{[(])}"
	print(correct_parenthesis(s=x))
